--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE setbox;
--
-- Name: setbox; Type: DATABASE; Schema: -; Owner: edvardsmazprecnieks
--

CREATE DATABASE setbox WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = icu LOCALE = 'en_US.UTF-8' ICU_LOCALE = 'en-US';


ALTER DATABASE setbox OWNER TO edvardsmazprecnieks;

\connect setbox

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: files; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.files (
    lesson_id integer NOT NULL,
    info character varying(255) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.files OWNER TO edvardsmazprecnieks;

--
-- Name: files_id_seq; Type: SEQUENCE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE SEQUENCE public.files_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.files_id_seq OWNER TO edvardsmazprecnieks;

--
-- Name: files_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edvardsmazprecnieks
--

ALTER SEQUENCE public.files_id_seq OWNED BY public.files.id;


--
-- Name: lesson; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.lesson (
    id integer NOT NULL,
    subject_id integer NOT NULL,
    date date NOT NULL,
    progress integer
);


ALTER TABLE public.lesson OWNER TO edvardsmazprecnieks;

--
-- Name: lesson_id_seq; Type: SEQUENCE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE SEQUENCE public.lesson_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lesson_id_seq OWNER TO edvardsmazprecnieks;

--
-- Name: lesson_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edvardsmazprecnieks
--

ALTER SEQUENCE public.lesson_id_seq OWNED BY public.lesson.id;


--
-- Name: studygroup; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.studygroup (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.studygroup OWNER TO edvardsmazprecnieks;

--
-- Name: studygroup_id_seq; Type: SEQUENCE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE SEQUENCE public.studygroup_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.studygroup_id_seq OWNER TO edvardsmazprecnieks;

--
-- Name: studygroup_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edvardsmazprecnieks
--

ALTER SEQUENCE public.studygroup_id_seq OWNED BY public.studygroup.id;


--
-- Name: subjects; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.subjects (
    name character varying(255) NOT NULL,
    id integer NOT NULL,
    user_id integer NOT NULL,
    studygroup_id integer
);


ALTER TABLE public.subjects OWNER TO edvardsmazprecnieks;

--
-- Name: subjects_id_seq; Type: SEQUENCE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE SEQUENCE public.subjects_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subjects_id_seq OWNER TO edvardsmazprecnieks;

--
-- Name: subjects_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edvardsmazprecnieks
--

ALTER SEQUENCE public.subjects_id_seq OWNED BY public.subjects.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.users (
    email character varying(255),
    name character varying(255),
    id integer NOT NULL
);


ALTER TABLE public.users OWNER TO edvardsmazprecnieks;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO edvardsmazprecnieks;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: edvardsmazprecnieks
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: users_in_studygroup; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.users_in_studygroup (
    studygroup_id integer NOT NULL,
    user_id integer NOT NULL
);


ALTER TABLE public.users_in_studygroup OWNER TO edvardsmazprecnieks;

--
-- Name: files id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.files ALTER COLUMN id SET DEFAULT nextval('public.files_id_seq'::regclass);


--
-- Name: lesson id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson ALTER COLUMN id SET DEFAULT nextval('public.lesson_id_seq'::regclass);


--
-- Name: studygroup id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.studygroup ALTER COLUMN id SET DEFAULT nextval('public.studygroup_id_seq'::regclass);


--
-- Name: subjects id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects ALTER COLUMN id SET DEFAULT nextval('public.subjects_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: files; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--



--
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

INSERT INTO public.lesson VALUES (4, 3, '2023-03-12', 90);
INSERT INTO public.lesson VALUES (5, 4, '2023-02-17', NULL);
INSERT INTO public.lesson VALUES (6, 3, '2023-01-25', 60);


--
-- Data for Name: studygroup; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--



--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

INSERT INTO public.subjects VALUES ('Math', 3, 1, NULL);
INSERT INTO public.subjects VALUES ('English', 4, 1, NULL);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

INSERT INTO public.users VALUES ('Edvards', 'edvards@edvards.lv', 1);


--
-- Data for Name: users_in_studygroup; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--



--
-- Name: files_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.files_id_seq', 1, false);


--
-- Name: lesson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.lesson_id_seq', 6, true);


--
-- Name: studygroup_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.studygroup_id_seq', 1, false);


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.subjects_id_seq', 4, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: files files_id_key; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_id_key UNIQUE (id);


--
-- Name: files files_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_pkey PRIMARY KEY (id);


--
-- Name: lesson lesson_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_pkey PRIMARY KEY (id);


--
-- Name: studygroup studygroup_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.studygroup
    ADD CONSTRAINT studygroup_pkey PRIMARY KEY (id);


--
-- Name: subjects subjects_id_key; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_id_key UNIQUE (id);


--
-- Name: subjects subjects_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_pkey PRIMARY KEY (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_id_key; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_id_key UNIQUE (id);


--
-- Name: users_in_studygroup users_in_studygroup_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users_in_studygroup
    ADD CONSTRAINT users_in_studygroup_pkey PRIMARY KEY (studygroup_id, user_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: files files_lesson_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.files
    ADD CONSTRAINT files_lesson_id_fkey FOREIGN KEY (lesson_id) REFERENCES public.lesson(id);


--
-- Name: lesson lesson_subject_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_subject_id_fkey FOREIGN KEY (subject_id) REFERENCES public.subjects(id);


--
-- Name: subjects subjects_studygroup_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_studygroup_id_fkey FOREIGN KEY (studygroup_id) REFERENCES public.studygroup(id);


--
-- Name: subjects subjects_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- Name: users_in_studygroup users_in_studygroup_studygroup_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users_in_studygroup
    ADD CONSTRAINT users_in_studygroup_studygroup_id_fkey FOREIGN KEY (studygroup_id) REFERENCES public.studygroup(id);


--
-- Name: users_in_studygroup users_in_studygroup_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users_in_studygroup
    ADD CONSTRAINT users_in_studygroup_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

