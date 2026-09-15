BEGIN;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE SCHEMA IF NOT EXISTS kordaxis;


CREATE TABLE IF NOT EXISTS kordaxis.raw_payloads (
    sha256 TEXT PRIMARY KEY,

    content BYTEA NOT NULL,

    size_bytes BIGINT
        GENERATED ALWAYS AS (
            octet_length(content)
        ) STORED,

    first_persisted_at TIMESTAMPTZ
        NOT NULL
        DEFAULT clock_timestamp(),

    CONSTRAINT raw_payload_sha256_format
        CHECK (
            sha256 ~ '^[0-9a-f]{64}$'
        ),

    CONSTRAINT raw_payload_sha256_matches_content
        CHECK (
            sha256
            =
            encode(
                digest(content, 'sha256'),
                'hex'
            )
        )
);


CREATE TABLE IF NOT EXISTS kordaxis.raw_event_envelopes (
    envelope_id TEXT PRIMARY KEY,

    source_id TEXT NOT NULL,

    source_event_id TEXT,

    source_timestamp TIMESTAMPTZ,

    received_at TIMESTAMPTZ NOT NULL,

    media_type TEXT NOT NULL,

    ingest_sequence BIGINT
        GENERATED ALWAYS AS IDENTITY,

    payload_sha256 TEXT NOT NULL,

    ingest_contract_version TEXT NOT NULL,

    persisted_at TIMESTAMPTZ
        NOT NULL
        DEFAULT clock_timestamp(),

    CONSTRAINT raw_event_envelopes_ingest_sequence_key
        UNIQUE (ingest_sequence),

    CONSTRAINT raw_event_envelopes_payload_fk
        FOREIGN KEY (payload_sha256)
        REFERENCES kordaxis.raw_payloads (sha256)
        ON UPDATE RESTRICT
        ON DELETE RESTRICT,

    CONSTRAINT raw_event_envelope_id_non_empty
        CHECK (
            btrim(envelope_id) <> ''
        ),

    CONSTRAINT raw_event_source_id_non_empty
        CHECK (
            btrim(source_id) <> ''
        ),

    CONSTRAINT raw_event_source_event_id_non_empty
        CHECK (
            source_event_id IS NULL
            OR btrim(source_event_id) <> ''
        ),

    CONSTRAINT raw_event_media_type_non_empty
        CHECK (
            btrim(media_type) <> ''
        ),

    CONSTRAINT raw_event_contract_version_non_empty
        CHECK (
            btrim(ingest_contract_version) <> ''
        )
);


CREATE INDEX IF NOT EXISTS
    raw_event_envelopes_source_event_idx
ON kordaxis.raw_event_envelopes (
    source_id,
    source_event_id
)
WHERE source_event_id IS NOT NULL;


CREATE OR REPLACE FUNCTION
    kordaxis.reject_raw_evidence_mutation()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE EXCEPTION
        'raw evidence is append-only: % on %.%',
        TG_OP,
        TG_TABLE_SCHEMA,
        TG_TABLE_NAME
        USING ERRCODE = '55000';
END;
$$;


DROP TRIGGER IF EXISTS
    raw_payloads_append_only
ON kordaxis.raw_payloads;

CREATE TRIGGER raw_payloads_append_only
BEFORE UPDATE OR DELETE OR TRUNCATE
ON kordaxis.raw_payloads
FOR EACH STATEMENT
EXECUTE FUNCTION
    kordaxis.reject_raw_evidence_mutation();


DROP TRIGGER IF EXISTS
    raw_event_envelopes_append_only
ON kordaxis.raw_event_envelopes;

CREATE TRIGGER raw_event_envelopes_append_only
BEFORE UPDATE OR DELETE OR TRUNCATE
ON kordaxis.raw_event_envelopes
FOR EACH STATEMENT
EXECUTE FUNCTION
    kordaxis.reject_raw_evidence_mutation();


REVOKE
    UPDATE,
    DELETE,
    TRUNCATE
ON kordaxis.raw_payloads
FROM PUBLIC;


REVOKE
    UPDATE,
    DELETE,
    TRUNCATE
ON kordaxis.raw_event_envelopes
FROM PUBLIC;


COMMIT;