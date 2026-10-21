# Orthosphere · protótipo da visão do médico

Protótipo navegável de front-end da **Orthosphere**, plataforma que integra a jornada do paciente ortopédico, do trauma à recuperação. Feito para demonstração em pitch. **Todos os dados são fictícios** e não há back-end.

## Telas
1. **Casos** · acionamento do médico e aceite do caso
2. **Paciente** · prontuário, laudos e encaminhamento, cuidados específicos
3. **Planejamento** · modelo do membro, ângulo de correção, simulação e escolha do implante
4. **Impressão** · impressão 3D com status em tempo real, kit da sala e caixa inteligente, cirurgia realizada
5. **Pós-op** · recuperação com Saúde+, fontes de dados e marco final

## Como abrir
Abra `index.html` com duplo clique. A fonte Outfit vem do Google Fonts, então precisa de internet.

## Publicar no GitHub Pages
Settings → Pages → Source: *Deploy from a branch* → Branch `main`, pasta `/ (root)` → Save.

## QR code
```bash
pip install segno
python gerar_qr.py https://SUA-URL-PUBLICADA
```
Gera `qr_orthosphere.png` com fundo branco e módulos navy.
