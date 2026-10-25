# idp-exemplo-api

Serviço de exemplo do **plat-idplabs**, usado para validar no homelab o modelo de CI/CD e GitOps da ADR-0006.

## O que tem aqui

```
platform.yaml                      # configuração única do repositório
apps/exemplo-api/
  service.yaml                     # descritor de serviço (ADR-0003)
  app/  tests/  Dockerfile
deploy/exemplo-api/
  base/                            # Deployment + Service; a release fixa a imagem por digest
  overlays/dev  overlays/prod
.github/workflows/ci.yml           # gatilho fino, sem configuração
```

## Fluxo

1. PR → `check` roda os gates do nível 2.
2. Merge na `main` → `release` calcula a versão pelos commits, publica `ghcr.io/mcavalcanti81/exemplo-api`, fixa o digest em `deploy/exemplo-api/base` e cria a tag `vX.Y.Z`.
3. Promoção → PR no `idp-ambientes` trocando a tag do ambiente.

Mensagens de commit seguem [Conventional Commits](https://www.conventionalcommits.org/pt-br/): `fix:` gera patch, `feat:` gera minor, `!` ou `BREAKING CHANGE:` gera major.

## Rodar localmente

```bash
cd apps/exemplo-api
uv run uvicorn app.main:app --reload
```
