--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

-- Started on 2020-07-14 10:44:09

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

--
-- TOC entry 2829 (class 0 OID 17084)
-- Dependencies: 203
-- Data for Name: Persons; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (2, 'test2', 'm', 1999, 2050, 'test', 'test', 'test', 'test');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (3, 'test3', 'f', 2001, 2051, 'test', 'teat', 'test', 'test');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (10, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (11, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (12, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (13, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (1, 'alaa', 'f', 1998, 2050, 'test', 'ahsaa', 'um hassan', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (14, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (15, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (16, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (17, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (18, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (19, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (20, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (21, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (22, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (23, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (24, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (25, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (26, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (27, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (28, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (29, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (30, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (31, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');
INSERT INTO public."Persons" (person_id, name, gender, day_of_birth, day_of_death, notes, address, nickname, status) VALUES (32, 'ali', 'm', 1994, 2050, 'test', 'ahsaa', 'bo jafer', 'live');


--
-- TOC entry 2831 (class 0 OID 17095)
-- Dependencies: 205
-- Data for Name: Relations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (1, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (2, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (3, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (7, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (8, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (9, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (10, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (11, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (12, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (13, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (14, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (15, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (16, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (17, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (18, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (19, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (20, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (21, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (22, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (23, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (24, 1, 2, 3);
INSERT INTO public."Relations" (relation_id, person, partenr, relation) VALUES (25, 1, 2, 3);


--
-- TOC entry 2839 (class 0 OID 0)
-- Dependencies: 202
-- Name: Persons_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Persons_person_id_seq"', 32, true);


--
-- TOC entry 2840 (class 0 OID 0)
-- Dependencies: 204
-- Name: Relations_relation_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Relations_relation_id_seq"', 25, true);


-- Completed on 2020-07-14 10:44:09

--
-- PostgreSQL database dump complete
--

