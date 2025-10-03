import json

print("🚀 Iniciando o super arquiteto de carreiras...")

# --- TRILHA 1: DESENVOLVIMENTO DE SOFTWARE (JÁ EXISTENTE E MELHORADA) ---
trilha_dev_software = {
    "trackId": "dev_software",
    "trackName": "Desenvolvimento de Software",
    "trackDescription": "Criação de aplicações, sistemas e websites através de linguagens de programação.",
    "nodes": [
        {"id": "dev_jr", "label": "Desenvolvedor(a) Júnior", "level": 1, "description": "Profissional em início de carreira, focado em aprender as tecnologias principais e resolver tarefas de menor complexidade com supervisão.", "skills": {"hard": ["Git e GitHub", "HTML5 e CSS3", "JavaScript Básico", "Lógica de Programação", "Consumir APIs REST"], "soft": ["Comunicação", "Trabalho em Equipe", "Proatividade para Aprender"]}},
        {"id": "dev_pl", "label": "Desenvolvedor(a) Pleno", "level": 2, "description": "Possui independência para desenvolver funcionalidades complexas. Começa a entender a arquitetura do sistema e a tomar decisões de design de código.", "skills": {"hard": ["JavaScript Avançado (ES6+)", "Frameworks (React, Vue ou Angular)", "Testes Unitários", "Pré-processadores CSS", "Design Patterns"], "soft": ["Resolução de Problemas", "Mentoria de Juniores", "Gerenciamento de Tempo"]}},
        {"id": "dev_sr", "label": "Engenheiro(a) de Software Sênior", "level": 3, "description": "Referência técnica no time. Lida com os desafios mais complexos, define arquiteturas, e tem uma visão de longo prazo sobre o produto e a tecnologia.", "skills": {"hard": ["Arquitetura de Sistemas", "Otimização de Performance", "Estratégias de Cache", "CI/CD (Automação)", "Microsserviços"], "soft": ["Liderança Técnica", "Visão de Negócio", "Tomada de Decisão Estratégica"]}},
        {"id": "tech_lead", "label": "Tech Lead", "level": 4, "description": "Líder técnico do time, responsável por garantir a qualidade técnica das entregas, guiar a equipe em decisões e remover impedimentos técnicos.", "skills": {"hard": ["Gestão de Projetos Ágeis", "Code Review Avançado", "Definição de Padrões", "Monitoramento e Observabilidade"], "soft": ["Liderança de Pessoas", "Comunicação com Stakeholders", "Resolução de Conflitos"]}},
        {"id": "architect", "label": "Arquiteto(a) de Software", "level": 4, "description": "Responsável pela visão macro da arquitetura de múltiplos sistemas. Define as tecnologias, padrões e o design de alto nível.", "skills": {"hard": ["Modelagem de Sistemas Distribuídos", "Padrões de Arquitetura", "Cloud (AWS, Azure, GCP)", "Segurança da Informação"], "soft": ["Pensamento Sistêmico", "Negociação", "Influência Técnica"]}}
    ],
    "edges": [{"from": "dev_jr", "to": "dev_pl"}, {"from": "dev_pl", "to": "dev_sr"}, {"from": "dev_sr", "to": "tech_lead"}, {"from": "dev_sr", "to": "architect"}]
}

# --- TRILHA 2: CIÊNCIA DE DADOS ---
trilha_ciencia_dados = {
    "trackId": "data_science",
    "trackName": "Ciência de Dados",
    "trackDescription": "Análise de grandes volumes de dados para extrair insights, criar modelos preditivos e suportar decisões de negócio.",
    "nodes": [
        {"id": "data_analyst_jr", "label": "Analista de Dados Júnior", "level": 1, "description": "Coleta, limpa e analisa dados para gerar relatórios e dashboards. Utiliza ferramentas como SQL, Excel e Power BI/Tableau.", "skills": {"hard": ["SQL para Consultas", "Excel Avançado", "Ferramentas de BI", "Estatística Descritiva", "Python (Pandas)"], "soft": ["Atenção aos Detalhes", "Raciocínio Lógico", "Curiosidade"]}},
        {"id": "data_analyst_sr", "label": "Analista de Dados Sênior", "level": 2, "description": "Conduz análises complexas, desenvolve hipóteses e apresenta insights para áreas de negócio. Automatiza processos de coleta de dados.", "skills": {"hard": ["Modelagem de Dados", "Testes A/B", "Python para Automação", "Visualização de Dados Avançada"], "soft": ["Storytelling com Dados", "Pensamento Crítico", "Autonomia"]}},
        {"id": "data_scientist", "label": "Cientista de Dados", "level": 3, "description": "Aplica técnicas estatísticas e de Machine Learning para criar modelos preditivos. Trabalha com problemas de negócio não estruturados.", "skills": {"hard": ["Machine Learning (Scikit-learn)", "Estatística Inferencial", "Álgebra Linear", "Ferramentas de Big Data (Spark)"], "soft": ["Resolução de Problemas Complexos", "Comunicação Técnica", "Visão de Produto"]}},
        {"id": "ml_specialist", "label": "Especialista em Machine Learning", "level": 4, "description": "Focado em construir, treinar e colocar em produção modelos de Machine Learning de alta performance e escalabilidade.", "skills": {"hard": ["Deep Learning (TensorFlow/PyTorch)", "MLOps", "Sistemas em Nuvem para IA", "Otimização de Algoritmos"], "soft": ["Inovação", "Pesquisa e Desenvolvimento", "Mentoria Especializada"]}}
    ],
    "edges": [{"from": "data_analyst_jr", "to": "data_analyst_sr"}, {"from": "data_analyst_sr", "to": "data_scientist"}, {"from": "data_scientist", "to": "ml_specialist"}]
}

# --- TRILHA 3: CONTABILIDADE ---
trilha_contabilidade = {
    "trackId": "contabilidade",
    "trackName": "Contabilidade",
    "trackDescription": "Garante a saúde financeira e a conformidade fiscal das empresas através do registro e análise de transações.",
    "nodes": [
        {"id": "cont_assist", "label": "Assistente Contábil", "level": 1, "description": "Auxilia em lançamentos, conciliações bancárias, organização de documentos e na preparação de relatórios básicos.", "skills": {"hard": ["Lançamentos Contábeis", "Conciliação Bancária", "Sistemas ERP (Básico)", "Pacote Office"], "soft": ["Organização", "Foco", "Ética Profissional"]}},
        {"id": "cont_analyst_jr", "label": "Analista Contábil Júnior", "level": 2, "description": "Responsável por apuração de impostos, fechamentos mensais e análise de contas patrimoniais.", "skills": {"hard": ["Apuração de Impostos (Simples, Lucro Presumido)", "Normas Contábeis (CPCs)", "Fechamento Contábil"], "soft": ["Análise Crítica", "Responsabilidade", "Comunicação Clara"]}},
        {"id": "cont_analyst_sr", "label": "Analista Contábil Sênior", "level": 3, "description": "Elabora demonstrações financeiras complexas (DRE, Balanço Patrimonial), atende auditorias e analisa a performance financeira.", "skills": {"hard": ["Demonstrações Financeiras", "Legislação Tributária Avançada", "Atendimento a Auditorias", "Planejamento Tributário"], "soft": ["Tomada de Decisão", "Visão Estratégica", "Gestão de Prazos"]}},
        {"id": "cont_controller", "label": "Controller / Gerente Contábil", "level": 4, "description": "Lidera a equipe contábil e fiscal, sendo o guardião das informações financeiras da empresa perante a diretoria e o mercado.", "skills": {"hard": ["Gestão de Equipe", "Orçamento e Projeções (FP&A)", "Relações com Investidores", "IFRS"], "soft": ["Liderança", "Visão de Negócio", "Inteligência Emocional"]}}
    ],
    "edges": [{"from": "cont_assist", "to": "cont_analyst_jr"}, {"from": "cont_analyst_jr", "to": "cont_analyst_sr"}, {"from": "cont_analyst_sr", "to": "cont_controller"}]
}

# --- TRILHA 4: ÁREA ADMINISTRATIVA ---
trilha_administrativa = {
    "trackId": "administrativo",
    "trackName": "Administrativo",
    "trackDescription": "Garante o bom funcionamento e a organização dos processos internos de uma empresa.",
    "nodes": [
        {"id": "adm_assist", "label": "Assistente Administrativo", "level": 1, "description": "Suporte em rotinas diárias, como controle de agenda, gestão de documentos, atendimento e organização do escritório.", "skills": {"hard": ["Pacote Office Avançado", "Gestão de E-mails e Agendas", "Organização de Arquivos", "Sistemas Internos"], "soft": ["Organização", "Comunicação Interpessoal", "Proatividade"]}},
        {"id": "adm_analyst", "label": "Analista Administrativo", "level": 2, "description": "Analisa e melhora processos, controla o orçamento da área, gera relatórios e gerencia contratos com fornecedores.", "skills": {"hard": ["Controle Orçamentário", "Gestão de Contratos", "Mapeamento de Processos (BPMN)", "Excel (Tabelas Dinâmicas)"], "soft": ["Resolução de Problemas", "Negociação", "Planejamento"]}},
        {"id": "adm_coord", "label": "Coordenador(a) Administrativo", "level": 3, "description": "Lidera a equipe administrativa, define metas, otimiza recursos e garante que as políticas da empresa sejam seguidas.", "skills": {"hard": ["Liderança de Equipes", "Gestão de Facilities", "Análise de Indicadores (KPIs)", "Planejamento Estratégico"], "soft": ["Delegação de Tarefas", "Visão Holística", "Gestão de Conflitos"]}},
        {"id": "adm_manager", "label": "Gerente Administrativo", "level": 4, "description": "Responsável por toda a infraestrutura e operação da empresa. Define o planejamento estratégico da área em alinhamento com a diretoria.", "skills": {"hard": ["Gestão Estratégica", "Análise de Viabilidade de Projetos", "Relacionamento com Diretoria", "Compliance"], "soft": ["Liderança Estratégica", "Tomada de Decisão de Alto Impacto", "Inteligência de Negócios"]}}
    ],
    "edges": [{"from": "adm_assist", "to": "adm_analyst"}, {"from": "adm_analyst", "to": "adm_coord"}, {"from": "adm_coord", "to": "adm_manager"}]
}

# --- TRILHA 5: RECURSOS HUMANOS ---
trilha_rh = {
    "trackId": "rh",
    "trackName": "Recursos Humanos",
    "trackDescription": "Atrai, desenvolve e retém os talentos que fazem a empresa crescer.",
    "nodes": [
        {"id": "rh_assist", "label": "Assistente de RH", "level": 1, "description": "Apoia em processos de recrutamento, agendamento de entrevistas, controle de ponto e benefícios.", "skills": {"hard": ["Controle de Ponto e Benefícios", "Triagem de Currículos", "Sistemas de RH (Básico)", "Onboarding de Funcionários"], "soft": ["Empatia", "Discrição", "Organização"]}},
        {"id": "rh_analyst", "label": "Analista de RH (Generalista)", "level": 2, "description": "Conduz processos seletivos, organiza treinamentos, realiza pesquisas de clima e apoia em avaliações de desempenho.", "skills": {"hard": ["Recrutamento e Seleção", "Treinamento e Desenvolvimento (T&D)", "Cargos e Salários", "Legislação Trabalhista"], "soft": ["Comunicação Assertiva", "Relacionamento Interpessoal", "Análise Crítica"]}},
        {"id": "rh_bp", "label": "Business Partner de RH", "level": 3, "description": "Atua como um consultor interno, alinhando as estratégias de RH com as necessidades específicas de uma área de negócio.", "skills": {"hard": ["Planejamento de Força de Trabalho", "Gestão de Desempenho", "Análise de Dados de RH", "Desenvolvimento de Lideranças"], "soft": ["Visão de Negócio", "Influência", "Parceria Estratégica"]}},
        {"id": "rh_manager", "label": "Gerente de RH", "level": 4, "description": "Lidera todas as frentes de Recursos Humanos, define a cultura organizacional e as estratégias de gestão de pessoas da empresa.", "skills": {"hard": ["Cultura Organizacional", "Estratégia de Remuneração", "Planejamento de Sucessão", "Relações Sindicais"], "soft": ["Liderança Inspiradora", "Visão Estratégica de Pessoas", "Gestão de Mudanças"]}}
    ],
    "edges": [{"from": "rh_assist", "to": "rh_analyst"}, {"from": "rh_analyst", "to": "rh_bp"}, {"from": "rh_bp", "to": "rh_manager"}]
}

# --- TRILHA 6: MARKETING DIGITAL ---
trilha_marketing_digital = {
    "trackId": "marketing_digital",
    "trackName": "Marketing Digital",
    "trackDescription": "Cria estratégias online para atrair clientes, gerar vendas e fortalecer a marca.",
    "nodes": [
        {"id": "mkt_assist", "label": "Assistente de Marketing", "level": 1, "description": "Cria posts para redes sociais, escreve textos para blogs, auxilia no disparo de e-mail marketing e gera relatórios básicos.", "skills": {"hard": ["Redes Sociais", "SEO (Básico)", "E-mail Marketing", "Google Analytics (Básico)"], "soft": ["Criatividade", "Boa Escrita", "Aprendizado Rápido"]}},
        {"id": "mkt_analyst", "label": "Analista de Marketing Digital", "level": 2, "description": "Gerencia campanhas de mídia paga (Google/Meta Ads), otimiza o site para buscas (SEO), e analisa o funil de vendas.", "skills": {"hard": ["Google Ads & Meta Ads", "SEO Técnico & Conteúdo", "Automação de Marketing", "Análise de Métricas (CAC, LTV)"], "soft": ["Pensamento Analítico", "Foco em Resultados", "Experimentação"]}},
        {"id": "mkt_specialist", "label": "Especialista em Marketing (Growth)", "level": 3, "description": "Profissional focado em encontrar alavancas de crescimento rápido, utilizando dados e experimentos para otimizar a aquisição de clientes.", "skills": {"hard": ["Growth Hacking", "Testes A/B", "Análise de Dados Avançada (SQL)", "Marketing de Produto"], "soft": ["Inovação", "Orientação a Dados", "Resiliência"]}},
        {"id": "mkt_manager", "label": "Gerente de Marketing", "level": 4, "description": "Lidera a equipe de marketing, define o orçamento, planeja as estratégias multicanal e é responsável pelos resultados de negócio da área.", "skills": {"hard": ["Planejamento Estratégico de Marketing", "Gestão de Orçamento (ROI)", "Liderança de Equipe", "Branding"], "soft": ["Liderança", "Visão de Mercado", "Comunicação com C-Level"]}}
    ],
    "edges": [{"from": "mkt_assist", "to": "mkt_analyst"}, {"from": "mkt_analyst", "to": "mkt_specialist"}, {"from": "mkt_specialist", "to": "mkt_manager"}]
}

# --- TRILHA 7: UI/UX DESIGN ---
trilha_design = {
    "trackId": "ui_ux_design",
    "trackName": "UI/UX Design",
    "trackDescription": "Cria experiências digitais fáceis e agradáveis de usar, desde a pesquisa com usuários até o design final das interfaces.",
    "nodes": [
        {"id": "design_jr", "label": "UI/UX Designer Júnior", "level": 1, "description": "Cria telas e componentes visuais (UI) com base em guias de estilo. Ajuda em pesquisas com usuários (UX) e na criação de wireframes.", "skills": {"hard": ["Figma/Sketch", "Princípios de Design Visual", "Wireframing", "Teoria das Cores", "Tipografia"], "soft": ["Empatia", "Atenção aos Detalhes", "Colaboração"]}},
        {"id": "design_pl", "label": "UI/UX Designer Pleno", "level": 2, "description": "Conduz o processo de design de ponta a ponta para uma funcionalidade, desde a pesquisa e ideação até a prototipagem e testes.", "skills": {"hard": ["Pesquisa com Usuários", "Jornada do Usuário", "Arquitetura da Informação", "Prototipagem Interativa", "Testes de Usabilidade"], "soft": ["Resolução de Problemas", "Comunicação de Decisões de Design", "Autonomia"]}},
        {"id": "design_sr", "label": "UI/UX Designer Sênior", "level": 3, "description": "Lidera projetos complexos, mentora outros designers e contribui para a estratégia do produto. É responsável pelo Design System.", "skills": {"hard": ["Design Systems", "Estratégia de UX", "Métricas de Produto", "Facilitação de Workshops", "Acessibilidade"], "soft": ["Liderança de Design", "Pensamento Crítico", "Influência"]}},
        {"id": "product_designer", "label": "Product Designer", "level": 4, "description": "Um Sênior com forte visão de negócio. Trabalha junto com Gerentes de Produto e Engenheiros para definir o 'o quê' e o 'porquê' construir.", "skills": {"hard": ["Estratégia de Produto", "Análise de Concorrentes", "Validação de Hipóteses de Negócio", "Data-driven Design"], "soft": ["Visão de Negócio", "Colaboração Multidisciplinar", "Storytelling"]}}
    ],
    "edges": [{"from": "design_jr", "to": "design_pl"}, {"from": "design_pl", "to": "design_sr"}, {"from": "design_sr", "to": "product_designer"}]
}

# --- JUNTANDO TUDO ---
# Agora criamos uma lista com todas as nossas trilhas de carreira.
all_tracks = [
    trilha_dev_software,
    trilha_ciencia_dados,
    trilha_contabilidade,
    trilha_administrativa,
    trilha_rh,
    trilha_marketing_digital,
    trilha_design
]

# Salvando a lista completa no nosso arquivo JSON.
try:
    with open('career_path.json', 'w', encoding='utf-8') as f:
        json.dump(all_tracks, f, ensure_ascii=False, indent=4)
    print("✅ Sucesso! O arquivo 'career_path.json' foi atualizado com as seguintes trilhas:")
    for track in all_tracks:
        print(f"  - {track['trackName']}")
except Exception as e:
    print(f"❌ Erro ao criar o arquivo JSON: {e}")