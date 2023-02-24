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
-- Name: subjects; Type: TABLE; Schema: public; Owner: edvardsmazprecnieks
--

CREATE TABLE public.subjects (
    id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(255) NOT NULL
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
    id integer NOT NULL,
    email character varying(255),
    name character varying(255)
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
-- Name: subjects id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects ALTER COLUMN id SET DEFAULT nextval('public.subjects_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: subjects; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

COPY public.subjects (id, user_id, name) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: edvardsmazprecnieks
--

COPY public.users (id, email, name) FROM stdin;
\.


--
-- Name: subjects_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.subjects_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: edvardsmazprecnieks
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: users id; Type: CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT id UNIQUE (id);


--
-- Name: subjects subjects_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: edvardsmazprecnieks
--

ALTER TABLE ONLY public.subjects
    ADD CONSTRAINT subjects_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

