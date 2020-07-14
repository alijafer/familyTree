#!/bin/bash
export AUTH0_DOMAIN='alidev.eu.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='familyTreeApi'
# username: postgres, password: 1, database_host: localhost:5432, database_name: famliytree_test
export DATABASE_URL='postgresql://postgres:1@localhost:5432/famliytree_test'
export FLASK_APP=app.py
export FLASK_DEBUG=true
export token-admin=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5aWnZlbTNiMDVxR2hra0t1MUJldiJ9.eyJpc3MiOiJodHRwczovL2FsaWRldi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWViZmEyMmI4YjIzOWQwYmZlNmRlMGY4IiwiYXVkIjoiZmFtaWx5VHJlZUFwaSIsImlhdCI6MTU5NDcxNDk3MCwiZXhwIjoxNTk0ODAxMzcwLCJhenAiOiJrTUNyVHJpUDNzYnhINXZQaWR4eUhQQmxIbFFOZUMyQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnBhcnRlbnIiLCJkZWxldGU6cGVyc29uIiwiZ2V0OnBhcnRlbnIiLCJnZXQ6cGVyc29uIiwicGF0Y2g6cGFydGVuciIsInBhdGNoOnBlcnNvbiIsInBvc3Q6cGFydGVuciIsInBvc3Q6cGVyc29uIl19.NkgzOHs8kHbkd5A7REAQSV7WjuAm6w4DdEAjyto_-SjdiIb8ixAGLFXHTOIyr8ZeVAiVE4CyoidYSyjN36HH7WcfgAfGpNYpOmvIc-2yod1SYox2kPlRmQMX88pSgwDHm96pj4h_qIA5sbsAvDuYXYxo454obl6EisAekjZ0ZcuSL6bxXLCaa1FxhkjjJbl5t1tRTUkOALABEzax_95r3glvEmaxuvS4ob9NqfD7BSOQFR8NBFenUOo25pcEhp6XodAq06HLHHNGgUpgfYjESQNLvsZPYg9miRD2yJfFH6zPeL2LDzC83C6nLPwBUh7Ow-YDufnjMhVWTZnYWYwQIw
export token-admin-lite=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5aWnZlbTNiMDVxR2hra0t1MUJldiJ9.eyJpc3MiOiJodHRwczovL2FsaWRldi5ldS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVjZDdiMDMyZjg3MDMwYzIwY2ZlMjI0IiwiYXVkIjoiZmFtaWx5VHJlZUFwaSIsImlhdCI6MTU5NDcxNjQ1NiwiZXhwIjoxNTk0ODAyODU2LCJhenAiOiJrTUNyVHJpUDNzYnhINXZQaWR4eUhQQmxIbFFOZUMyQyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OnBhcnRlbnIiLCJnZXQ6cGVyc29uIiwicG9zdDpwYXJ0ZW5yIiwicG9zdDpwZXJzb24iXX0.Rot8NKV5Hrfg9WfcjxyN-nwRiZPxoWKbZWyMgBZ8RgpSekZAtsbKWZ8--E0USqkr2CoFgeThjiyWGAhhuAGgjYiLcANPRx7QDWVttBPMExWSbHMLgSrVfhUTM5-08iGh2rbVcKpXE06Oc6IxCTqZJFYpOGfY4UAubqKMgmW3q0x5ZqFHk-IczOsk5RK47AVfa4bBYxUCLSOhK74jvTgqqWdadf4X9AlsJuny-0JihviWFygEYVdBQZhDwmM1QyGfyUGDHWOrthNq5zVLqTs6KmB7MRl2e1_3yvGb2ittcs-FnAA76uJJ7AO8sNWYJRbvwhapOV23x4a5jJCp8MFnLQ