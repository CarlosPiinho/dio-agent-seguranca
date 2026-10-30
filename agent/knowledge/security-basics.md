# Fundamentos de Segurança da Informação (base de conhecimento)

Arquivo de consulta do agente. Reúne os conceitos, as classificações e as boas práticas que sustentam a skill `vulnerability-analysis`.

## Como usar este arquivo

- Consulte-o para **explicar conceitos** e **fundamentar** a análise, sempre adaptando a profundidade ao nível da pessoa (iniciante, intermediário ou avançado). Não despeje o conteúdo inteiro: use só o que a pergunta pede.
- Prefira **explicar com analogia primeiro** e entrar no detalhe técnico depois.
- IDs de CWE, técnicas do MITRE ATT&CK, categorias do OWASP e comandos aqui listados são **pontos de partida**. Se houver dúvida sobre um ID, versão ou comportamento, diga "verificar na fonte oficial" (veja a seção *Fontes oficiais*) em vez de afirmar com certeza.
- Os exemplos servem para **defesa e aprendizado**, em ambientes próprios, de laboratório ou autorizados.

---

## 1. Conceitos centrais

### Analogia da casa

| Conceito | Na casa | Em sistemas |
|---|---|---|
| **Ativo** | A casa e o que há dentro dela | Dados, aplicação, servidor, credenciais |
| **Vulnerabilidade** | Uma janela destrancada | Falha no código, na configuração ou no processo |
| **Ameaça** | Alguém com intenção de entrar | Atacante, malware, erro humano, falha de hardware |
| **Risco** | A chance de entrarem pela janela × o prejuízo | Probabilidade × impacto |
| **Controle** | Trancar a janela, instalar alarme | Correção, firewall, MFA, monitoramento |

### Definições

- **Ativo:** qualquer coisa que tenha valor e precise ser protegida.
- **Vulnerabilidade:** fraqueza que pode ser explorada. Por si só, não causa dano.
- **Ameaça:** qualquer evento ou agente capaz de explorar uma vulnerabilidade e causar dano.
- **Exploit:** técnica ou código que aproveita uma vulnerabilidade.
- **Risco:** possibilidade de perda, resultado da combinação entre probabilidade e impacto. **Sem vulnerabilidade ou sem ameaça, o risco é baixo; com as duas e um ativo valioso, é alto.**
- **Superfície de ataque:** conjunto de pontos por onde um atacante pode tentar entrar (portas abertas, formulários, APIs, contas). Reduzir a superfície reduz o risco.
- **Vetor de ataque:** o caminho usado (rede, e-mail, formulário web, acesso físico).
- **Controle (ou mitigação):** medida que reduz a probabilidade ou o impacto.
- **Risco residual:** o que sobra depois dos controles. Nenhum sistema tem risco zero.

### Tratamento de risco

Diante de um risco, as opções são: **mitigar** (reduzir com controles), **aceitar** (conscientemente, quando é baixo), **transferir** (ex.: seguro, terceirização) ou **evitar** (eliminar a atividade).

---

## 2. A tríade CIA (confidencialidade, integridade e disponibilidade)

| Pilar | Pergunta | Exemplo de violação | Controles típicos |
|---|---|---|---|
| **Confidencialidade** | Só quem deve vê? | Vazamento de banco de clientes | Criptografia, controle de acesso, MFA |
| **Integridade** | O dado é confiável e não foi alterado indevidamente? | Alteração de saldo por um atacante | Hash, assinaturas, validação, logs de auditoria |
| **Disponibilidade** | O sistema está acessível quando necessário? | Ataque de negação de serviço, ransomware | Backups, redundância, limites de requisição |

**Como usar na análise:** ao avaliar o impacto de uma vulnerabilidade, pergunte quais dos três pilares são afetados e com que gravidade. Exemplo: SQL Injection em login pode afetar os três (ler dados, alterar dados, apagar tabelas).

### Autenticação, autorização e auditoria

- **Autenticação (AuthN):** provar quem você é (senha, chave, biometria, MFA).
- **Autorização (AuthZ):** definir o que você pode fazer depois de autenticado.
- **Auditoria (accountability):** registrar quem fez o quê e quando.

Confundir autenticação com autorização é uma das causas mais comuns de falhas de acesso.

---

## 3. Classificações e padrões (não confundir)

| Padrão | O que é | Pergunta que responde |
|---|---|---|
| **CWE** | Catálogo de **tipos de fraqueza** de software | "Que tipo de falha é esta?" (ex.: CWE-89) |
| **CVE** | Identificador de uma **vulnerabilidade específica e pública** em um produto/versão | "Qual é a falha conhecida neste software e versão?" (ex.: CVE-AAAA-NNNNN) |
| **CVSS** | **Pontuação de severidade** de 0 a 10 | "Quão grave é, em termos gerais?" |
| **OWASP Top 10** | Lista das **categorias de risco** mais críticas em aplicações web | "Em qual categoria ampla ela se encaixa?" |
| **MITRE ATT&CK** | Base de **táticas e técnicas** usadas por atacantes | "Como um atacante usaria isso?" |

> Atenção: o código `app.py` com SQL Injection **não tem CVE**, porque é uma falha no código de alguém, não uma vulnerabilidade catalogada em um produto. Nunca invente um CVE.

### CVSS: faixas de severidade

| Pontuação | Classificação |
|---|---|
| 0,0 | Nenhuma |
| 0,1 a 3,9 | Baixa |
| 4,0 a 6,9 | Média |
| 7,0 a 8,9 | Alta |
| 9,0 a 10,0 | Crítica |

O CVSS mede a severidade **técnica genérica**. A skill usa uma matriz própria de **impacto × probabilidade no contexto da pessoa**, que pode dar resultado diferente do CVSS (e tudo bem, desde que justificado).

### Matriz de severidade usada pela skill

| Probabilidade \ Impacto | Baixo | Médio | Alto |
|---|---|---|---|
| **Alta** | Média | Alta | **Crítica** |
| **Média** | Baixa | Média | Alta |
| **Baixa** | Baixa | Baixa | Média |

- **Impacto:** o que se perde em confidencialidade, integridade e disponibilidade.
- **Probabilidade:** exposição, facilidade de exploração, necessidade de autenticação, existência de exploit conhecido.
- **Contexto muda tudo:** exposição à internet e dados sensíveis sobem o nível; ambiente isolado de laboratório e dados fictícios descem.

### OWASP Top 10 (edição 2021)

| ID | Categoria |
|---|---|
| A01 | Broken Access Control (controle de acesso quebrado) |
| A02 | Cryptographic Failures (falhas criptográficas) |
| A03 | Injection (injeção) |
| A04 | Insecure Design (design inseguro) |
| A05 | Security Misconfiguration (configuração incorreta de segurança) |
| A06 | Vulnerable and Outdated Components (componentes vulneráveis e desatualizados) |
| A07 | Identification and Authentication Failures (falhas de identificação e autenticação) |
| A08 | Software and Data Integrity Failures (falhas de integridade de software e dados) |
| A09 | Security Logging and Monitoring Failures (falhas de log e monitoramento) |
| A10 | Server-Side Request Forgery (SSRF) |

> A lista é revisada periodicamente. Ao citar, indique a edição (ex.: "A03:2021") e, se necessário, recomende conferir a edição vigente em owasp.org.

### CWEs frequentes

| CWE | Fraqueza |
|---|---|
| CWE-89 | SQL Injection |
| CWE-79 | Cross-Site Scripting (XSS) |
| CWE-78 | Injeção de comandos do sistema operacional |
| CWE-22 | Path Traversal (acesso a arquivos fora do diretório permitido) |
| CWE-352 | Cross-Site Request Forgery (CSRF) |
| CWE-287 | Autenticação inadequada |
| CWE-306 | Falta de autenticação em função crítica |
| CWE-862 | Falta de autorização |
| CWE-307 | Falta de limite para tentativas excessivas de autenticação |
| CWE-256 | Armazenamento de senha em texto puro |
| CWE-916 | Hash de senha com esforço computacional insuficiente |
| CWE-798 | Credenciais fixas no código (hard-coded) |
| CWE-327 | Algoritmo criptográfico quebrado ou arriscado |
| CWE-200 | Exposição de informação sensível |
| CWE-209 | Exposição de informação em mensagens de erro |
| CWE-532 | Informação sensível gravada em logs |
| CWE-434 | Upload irrestrito de arquivos perigosos |
| CWE-502 | Desserialização de dados não confiáveis |
| CWE-918 | Server-Side Request Forgery (SSRF) |

### MITRE ATT&CK: as 14 táticas (Enterprise)

Reconnaissance, Resource Development, **Initial Access**, Execution, Persistence, Privilege Escalation, Defense Evasion, **Credential Access**, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration e Impact.

A **tática** é o objetivo do atacante (o "porquê"); a **técnica** é o método (o "como"), identificada por um ID `T####` (e subtécnicas `T####.###`).

| Cenário comum | Tática | Técnica (verificar ID em attack.mitre.org) |
|---|---|---|
| SQL Injection em aplicação exposta | Initial Access | T1190 Exploit Public-Facing Application |
| Uso de credenciais roubadas ou fracas | Initial Access / Persistence | T1078 Valid Accounts |
| Tentativas repetidas de senha (força bruta) | Credential Access | T1110 Brute Force |
| Serviço de acesso remoto exposto (ex.: SSH, RDP) | Initial Access | T1133 External Remote Services |
| Uso do SSH para movimentação | Lateral Movement | T1021 Remote Services (subtécnica .004, SSH) |
| Segredos esquecidos em arquivos ou código | Credential Access | T1552 Unsecured Credentials |
| Varredura de portas e serviços | Discovery | T1046 Network Service Discovery |
| Escalada de privilégios por falha em software | Privilege Escalation | T1068 Exploitation for Privilege Escalation |
| Negação de serviço | Impact | T1498 Network Denial of Service |
| Dados criptografados para extorsão | Impact | T1486 Data Encrypted for Impact |

> Se o cenário não aparecer na tabela, **não adivinhe o ID**: descreva a técnica pelo nome e indique para confirmar em attack.mitre.org.

---

## 4. Princípios de defesa

- **Defesa em profundidade:** várias camadas, de modo que a falha de uma não derrube tudo (validação de entrada + consulta parametrizada + menor privilégio no banco + logs).
- **Menor privilégio:** cada usuário, serviço e processo só tem o acesso mínimo necessário. Uma aplicação web não precisa de um usuário de banco que possa apagar tabelas.
- **Falhar de forma segura (fail secure):** na dúvida ou no erro, negar o acesso.
- **Nunca confiar na entrada:** todo dado vindo de fora (formulário, URL, cabeçalho, arquivo, API) é não confiável até ser validado.
- **Segurança por design:** pensar em segurança desde o desenho, não apenas no final.
- **Simplicidade:** menos código, menos serviços e menos portas significam menos superfície de ataque.
- **Segredos fora do código:** senhas, chaves e tokens em variáveis de ambiente ou em um cofre de segredos.
- **Mínima exposição de informação:** mensagens de erro genéricas ao usuário e detalhes só nos logs.

### Perguntas que um revisor de segurança faz ao ler código

1. De onde vem cada entrada de dados?
2. Para onde ela vai (banco, shell, arquivo, página HTML, outra API)?
3. Quem pode chamar esta função e há verificação de autenticação e autorização?
4. O que acontece quando dá erro? O que o usuário vê? O que fica nos logs?
5. Há segredos, senhas ou chaves no código ou em arquivos versionados?
6. Os dados sensíveis estão protegidos em repouso e em trânsito?
7. As dependências estão atualizadas e são realmente necessárias?

---

## 5. Vulnerabilidades comuns: causa raiz e correção

### 5.1 SQL Injection (CWE-89, OWASP A03, MITRE T1190)

**O que é:** a entrada da pessoa é concatenada na query e passa a ser interpretada como **código SQL**, e não como dado.

**Código vulnerável:**

```python
query = f"SELECT * FROM usuarios WHERE username = '{usuario}' AND password = '{senha}'"
cursor.execute(query)
```

**Lógica da exploração (conceitual):** se a entrada contiver uma aspa e uma condição sempre verdadeira, a consulta passa a ter outro significado e a checagem de senha pode ser ignorada. Exemplo mínimo e didático de entrada no campo de usuário: `' OR '1'='1`. Em laboratório, serve apenas para mostrar por que o problema existe.

**Impacto possível:** burlar a autenticação (confidencialidade), alterar ou apagar dados (integridade e disponibilidade).

**Correção principal:** consulta parametrizada. O banco recebe a estrutura da query separada dos valores, que nunca são interpretados como código.

```python
cursor.execute(
    "SELECT * FROM usuarios WHERE username = ? AND password = ?",
    (usuario, senha)
)
```

**Defesa em profundidade:**
- Validar tipo, tamanho e formato da entrada.
- Usar um usuário de banco com o mínimo de permissões.
- Não exibir erros do banco ao usuário final.
- Preferir um ORM ou uma biblioteca de acesso que use parâmetros por padrão.

**Atenção:** parâmetros valem para **valores**, não para nomes de tabelas ou colunas. Se for preciso variar nomes, use uma **lista de permitidos (allowlist)** fixa no código.

**Como validar a correção:** repetir o teste com a entrada maliciosa (deve falhar), testar um login legítimo (deve funcionar) e revisar os logs.

### 5.2 Senhas em texto puro ou com hash fraco (CWE-256, CWE-916)

**Problema:** se o banco vazar, todas as senhas ficam expostas. Hashes rápidos e sem *salt* (como MD5 e SHA-1 puros) são quebrados com facilidade.

**Boa prática:** armazenar apenas o **hash** da senha, com algoritmo **lento e com salt**: **argon2**, **bcrypt** ou **scrypt**. Não confundir:

| | Criptografia | Hash |
|---|---|---|
| Reversível? | Sim, com a chave | Não |
| Uso | Proteger dados que precisam ser lidos depois | Verificar senhas |

**Exemplo de login mais seguro** (SQLite, `bcrypt` instalado com `pip install bcrypt`):

```python
import sqlite3
import bcrypt

def fazer_login(usuario, senha):
    conexao = sqlite3.connect('banco_de_dados.db')
    try:
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT password_hash FROM usuarios WHERE username = ?",
            (usuario,)
        )
        linha = cursor.fetchone()
    finally:
        conexao.close()

    if linha and bcrypt.checkpw(senha.encode('utf-8'), linha[0]):
        return "Acesso Permitido!"
    return "Usuário ou senha inválidos."   # mensagem genérica
```

Pontos de ensino: a consulta busca **só pelo usuário**; a senha é comparada pelo hash; a mensagem de erro é **genérica** (não revela se o usuário existe); a conexão fecha mesmo em caso de erro. Para o cadastro, gerar o hash com `bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())`.

**Complementos:** limitar tentativas de login (CWE-307) e oferecer MFA.

### 5.3 Cross-Site Scripting, XSS (CWE-79, OWASP A03)

**O que é:** dados não confiáveis são exibidos em uma página sem tratamento e o navegador executa o conteúdo como script.
**Correção:** *escapar* a saída conforme o contexto (HTML, atributo, JavaScript), usar frameworks que escapam por padrão e adotar uma Content Security Policy (CSP).

### 5.4 Injeção de comandos (CWE-78)

**O que é:** entrada do usuário montada em um comando do sistema operacional.
**Correção:** evitar chamar o shell; usar APIs da linguagem; quando inevitável, passar argumentos como **lista** (sem `shell=True` em Python), validar com allowlist.

```python
# Evite:
os.system(f"ping {host}")
# Prefira:
subprocess.run(["ping", "-c", "1", host], check=True)  # ainda validar 'host' com allowlist
```

### 5.5 Controle de acesso quebrado (CWE-862, OWASP A01)

**O que é:** o sistema autentica, mas não verifica se **aquela pessoa** pode acessar **aquele recurso** (ex.: trocar o número do pedido na URL e ver o pedido de outra pessoa; isso é conhecido como IDOR).
**Correção:** checar a autorização **no servidor**, a cada requisição, por recurso. Negar por padrão. Nunca confiar em dados vindos do cliente para decidir permissões.

### 5.6 Segredos no código (CWE-798)

**Problema:** senhas, chaves de API e tokens escritos no código e enviados ao repositório.
**Correção:** variáveis de ambiente ou cofre de segredos; arquivos como `.env` no `.gitignore`.
**Se um segredo vazou:** considere-o **comprometido**. **Rotacione** (gere outro e revogue o antigo). Apagar do histórico não basta. Não repita o valor na resposta.

### 5.7 Configuração insegura e componentes desatualizados (OWASP A05 e A06)

**Sinais:** credenciais padrão, modo debug em produção, portas desnecessárias abertas, listagem de diretórios, dependências antigas com falhas conhecidas.
**Correção:** hardening (remover o que não é usado), trocar padrões, atualizar com regularidade e acompanhar avisos de segurança dos componentes usados.

---

## 6. Hardening básico de servidor Linux (Ubuntu)

> Use apenas em servidores **próprios ou de laboratório**. Comandos marcados como **[diagnóstico]** só leem informações; os marcados como **[altera]** modificam o sistema e **exigem confirmação da pessoa antes de serem sugeridos para execução**. Nunca execute nada em hosts remotos.

### Diagnóstico (superfície e exposição)

```bash
ss -tulpn                    # [diagnóstico] portas abertas e processos que as usam
sudo ufw status verbose      # [diagnóstico] estado do firewall
sudo sshd -T | grep -Ei 'passwordauthentication|permitrootlogin|pubkeyauthentication'   # [diagnóstico] política efetiva do SSH
last -n 20                   # [diagnóstico] últimos logins
sudo grep "Failed password" /var/log/auth.log | tail   # [diagnóstico] tentativas de senha falhas
apt list --upgradable        # [diagnóstico] pacotes com atualização pendente
```

### Boas práticas e como aplicar

| Prática | Por quê | Comando de referência |
|---|---|---|
| **Atualizar o sistema** | Corrige falhas conhecidas | `sudo apt update && sudo apt upgrade` **[altera]** |
| **Atualizações de segurança automáticas** | Reduz a janela de exposição | pacote `unattended-upgrades` **[altera]** |
| **Firewall: negar por padrão** | Só entra o que for explicitamente permitido | `sudo ufw default deny incoming`, `sudo ufw allow OpenSSH`, `sudo ufw enable` **[altera]** |
| **SSH com chave, sem senha** | Elimina a força bruta de senhas | `PasswordAuthentication no` no `sshd_config` **[altera]** |
| **Desabilitar login direto do root** | Evita o alvo mais óbvio | `PermitRootLogin no` **[altera]** |
| **Usuário comum com `sudo`** | Menor privilégio e rastreabilidade | `adduser`, `usermod -aG sudo` **[altera]** |
| **Proteção contra força bruta** | Bloqueia IPs com muitas falhas | pacote `fail2ban` **[altera]** |
| **Remover serviços não usados** | Menos superfície de ataque | `sudo systemctl disable --now <servico>` **[altera]** |
| **Logs e monitoramento** | Detectar e investigar incidentes | `journalctl -u ssh`, `/var/log/auth.log` |

**Cuidados ao alterar o SSH (para não se trancar para fora):**
1. **Autorize o SSH no firewall antes de habilitá-lo.**
2. Confirme que o **login por chave funciona** antes de desligar a senha.
3. **Mantenha uma sessão aberta** enquanto testa a nova configuração em outra.
4. Valide a sintaxe com `sudo sshd -t` antes de reiniciar o serviço (`sudo systemctl restart ssh`).

---

## 7. Resposta a incidentes (visão geral)

Quando há suspeita de comprometimento, o ciclo geral é: **preparar → detectar → conter → erradicar → recuperar → aprender**.

- **Conter:** isolar o sistema afetado (desconectar da rede), sem apagar evidências.
- **Preservar evidências:** não desligar nem apagar logs sem necessidade; registrar horários.
- **Erradicar e recuperar:** remover a causa, restaurar a partir de backups confiáveis, trocar credenciais.
- **Aprender:** documentar a causa raiz e ajustar os controles.

Em ambientes reais de organizações, acione a equipe de segurança responsável. A skill é educativa e não substitui um processo formal de resposta a incidentes.

---

## 8. Erros comuns de iniciantes

- Achar que "validar no front-end" basta. A validação que protege é a do **servidor**.
- Tentar "limpar" entradas manualmente em vez de usar **consultas parametrizadas**.
- Guardar senhas em texto puro ou com MD5 e SHA-1 simples.
- Confundir **criptografia** com **hash**, e **autenticação** com **autorização**.
- Deixar segredos no código ou no repositório (inclusive no histórico do Git).
- Mostrar mensagens de erro detalhadas ao usuário final.
- Ignorar atualizações de dependências e do sistema.
- Dar ao banco ou ao serviço **mais permissões** do que o necessário.
- Tratar um scanner como verdade absoluta: ele tem falsos positivos e falsos negativos.
- Achar que "ninguém vai atacar um sistema pequeno". Varreduras automáticas atingem qualquer coisa exposta.

---

## 9. Mini-glossário

| Termo | Significado |
|---|---|
| **Allowlist** | Lista do que é permitido (mais segura que listar o que é proibido) |
| **ATT&CK** | Base de táticas e técnicas de atacantes, mantida pela MITRE |
| **Brute force** | Tentativa sistemática de adivinhar credenciais |
| **CIA** | Confidencialidade, integridade e disponibilidade |
| **CVE** | Identificador público de uma vulnerabilidade específica |
| **CVSS** | Sistema de pontuação de severidade (0 a 10) |
| **CWE** | Catálogo de tipos de fraqueza de software |
| **DAST** | Teste dinâmico, com a aplicação em execução |
| **DevSecOps** | Segurança integrada ao ciclo de desenvolvimento e entrega |
| **Exploit** | Código ou técnica que aproveita uma vulnerabilidade |
| **Hardening** | Endurecimento: reduzir superfície de ataque e reforçar configurações |
| **Hash** | Resumo de tamanho fixo, de via única, de um dado |
| **IDOR** | Acesso a objeto de outra pessoa trocando um identificador |
| **MFA** | Autenticação com mais de um fator (algo que sabe, tem ou é) |
| **Patch** | Correção publicada para uma falha |
| **Pentest** | Teste de intrusão autorizado, com escopo definido |
| **Salt** | Valor aleatório somado à senha antes do hash |
| **SAST** | Análise estática do código-fonte, sem executá-lo |
| **SIEM** | Plataforma que centraliza e correlaciona logs e alertas |
| **Zero-day** | Falha sem correção disponível, já explorada ou prestes a ser |

---

## 10. Fontes oficiais para conferência

- MITRE ATT&CK: attack.mitre.org
- MITRE CWE: cwe.mitre.org
- OWASP Top 10 e Cheat Sheet Series: owasp.org
- NVD (banco de CVEs e CVSS): nvd.nist.gov
- Documentação oficial do Ubuntu: ubuntu.com/server/docs

**Regra de ouro:** na dúvida sobre um ID, versão ou comportamento, o agente diz que **não tem certeza** e indica a fonte para conferir. Uma resposta honesta vale mais que uma resposta confiante e errada.