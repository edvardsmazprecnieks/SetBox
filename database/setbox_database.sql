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

SET default_tablespace = '';

SET default_table_access_method = heap;

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
-- Name: subjects; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.subjects (
    name character varying(255) NOT NULL,
    id integer NOT NULL,
    user_id integer NOT NULL
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
-- Name: lesson id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson ALTER COLUMN id SET DEFAULT nextval('public.lesson_id_seq'::regclass);


--
-- Name: subjects id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects ALTER COLUMN id SET DEFAULT nextval('public.subjects_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: lesson; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

COPY public.lesson (id, subject_id, date, progress) FROM stdin;
\.


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

COPY public.subjects (name, id, user_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

COPY public.users (email, name, id) FROM stdin;
\.


--
-- Name: lesson_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.lesson_id_seq', 1, false);


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.subjects_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: lesson lesson_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_pkey PRIMARY KEY (id);


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
-- Name: users users_id_key; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_id_key UNIQUE (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: lesson lesson_subject_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.lesson
    ADD CONSTRAINT lesson_subject_id_fkey FOREIGN KEY (subject_id) REFERENCES public.subjects(id);


--
-- Name: subjects subjects_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

