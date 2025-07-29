CREATE TABLE "compania" (
  "id" serial PRIMARY KEY,
  "company_name" text UNIQUE NOT NULL
);

CREATE TABLE "locacion" (
  "id" serial PRIMARY KEY,
  "job_location" text,
  "search_location" text,
  "job_country" text
);

CREATE TABLE "tipo_calendario" (
  "id" serial PRIMARY KEY,
  "job_schedule_type" text UNIQUE NOT NULL
);

CREATE TABLE "job" (
  "job_id" serial PRIMARY KEY,
  "job_title" text NOT NULL,
  "job_title_short" text,
  "job_via" text,
  "job_posted_date" timestamp,
  "job_work_from_home" boolean,
  "job_no_degree_mention" boolean,
  "job_health_insurance" boolean,
  "salary_rate" text,
  "salary_year_avg" numeric,
  "salary_hour_avg" numeric,
  "compania_id" int,
  "location_id" int,
  "tipo_calendario_id" int
);

CREATE TABLE "habilidades" (
  "skill_id" serial PRIMARY KEY,
  "skill_name" text UNIQUE NOT NULL
);

CREATE TABLE "tipo_habilidad" (
  "id" serial PRIMARY KEY,
  "type_name" text UNIQUE NOT NULL
);

CREATE TABLE "job_skill" (
  "job_id" int,
  "skill_id" int,
  "primary" key(job_id,skill_id)
);

CREATE TABLE "job_skill_type" (
  "job_id" int,
  "skill_id" int,
  "skill_type_id" int,
  "primary" key(job_id,skill_id,skill_type_id)
);

ALTER TABLE "job" ADD FOREIGN KEY ("compania_id") REFERENCES "compania" ("id");

ALTER TABLE "job" ADD FOREIGN KEY ("location_id") REFERENCES "locacion" ("id");

ALTER TABLE "job" ADD FOREIGN KEY ("tipo_calendario_id") REFERENCES "tipo_calendario" ("id");

ALTER TABLE "job_skill" ADD FOREIGN KEY ("job_id") REFERENCES "job" ("job_id");

ALTER TABLE "job_skill" ADD FOREIGN KEY ("skill_id") REFERENCES "habilidades" ("skill_id");

ALTER TABLE "job_skill_type" ADD FOREIGN KEY ("job_id") REFERENCES "job" ("job_id");

ALTER TABLE "job_skill_type" ADD FOREIGN KEY ("skill_id") REFERENCES "habilidades" ("skill_id");

ALTER TABLE "job_skill_type" ADD FOREIGN KEY ("skill_type_id") REFERENCES "tipo_habilidad" ("id");
