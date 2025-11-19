# YouTube ELT Pipeline com Airflow, Postgres e Soda Core

Este projeto implementa um pipeline ELT (Extract, Load, Transform) completo para coletar estatísticas de vídeos de um canal do YouTube, armazenar esses dados em um banco PostgreSQL organizado em camadas (staging e core) e validar a qualidade dos dados utilizando Soda Core.
Toda a orquestração é feita pelo Apache Airflow.