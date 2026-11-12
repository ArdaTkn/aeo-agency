def decompose_boss_directive(directive_text, target_deadline=None):
    """
    Project Manager (Sarah Jenkins) Cognitive Engine:
    Takes a high-level strategic directive from the Boss, decomposes it into 
    executable sub-tasks, assigns them to the appropriate specialist agents,
    and returns a structured execution sequence.
    """
    text_lower = directive_text.lower()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    subtasks = []

    # 1. PM Master Ticket
    subtasks.append({
        "task_id": f"TSK-PM-{int(time.time())}",
        "assigned_by": "Boss",
        "agent_name": "Sarah Jenkins (Agent 1: Project Manager)",
        "task_description": f"Master Directive Ingested: '{directive_text}'. Decomposed strategy into functional specialist workstreams.",
        "priority": "High",
        "status": "Completed",
        "output_link": "Command Center Pipeline",
        "completion_time": "10m"
    })

    # Pattern: Storefront / Business / City / Local Audit Directive
    if any(k in text_lower for k in ["riga", "store", "dükkan", "shop", "audit", "lead", "client", "business", "outreach", "prospect"]):
        # Agent 8: Outbound Lead
        subtasks.append({
            "task_id": f"TSK-LEAD-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Jordan Hayes (Agent 8: Outbound Growth Lead)",
            "task_description": f"Identify and qualify target accounts for directive: '{directive_text}'. Draft tailored outreach proposals.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/proposals",
            "completion_time": "25m"
        })
        # Agent 2: Researcher
        subtasks.append({
            "task_id": f"TSK-RES-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Marcus Vance (Agent 2: Lead LLM Researcher)",
            "task_description": f"Execute synthetic buyer prompt batteries on ChatGPT & Perplexity to map citation gaps for: '{directive_text}'.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/audits",
            "completion_time": "30m"
        })
        # Agent 3: Knowledge Architect
        subtasks.append({
            "task_id": f"TSK-KNOW-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Elena Rostova (Agent 3: Knowledge Architect)",
            "task_description": f"Generate machine-readable /llms.txt entity maps and LocalBusiness Schema.org JSON-LD microdata.",
            "priority": "Medium",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/specs",
            "completion_time": "40m"
        })
        # Agent 6: Technical Auditor
        subtasks.append({
            "task_id": f"TSK-TECH-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Alex Rivera (Agent 6: Technical AEO Auditor)",
            "task_description": f"Verify crawler access permissions (robots.txt, GPTBot, ClaudeBot) and validate schema syntax for directive.",
            "priority": "Medium",
            "status": "Completed",
            "output_link": "https://validator.schema.org",
            "completion_time": "20m"
        })

    # Pattern: Content, Comparison, Brand Consensus Directive
    elif any(k in text_lower for k in ["content", "post", "blog", "reddit", "article", "yazı", "içerik", "consensus", "pr"]):
        # Agent 3: Knowledge Architect
        subtasks.append({
            "task_id": f"TSK-KNOW-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Elena Rostova (Agent 3: Knowledge Architect)",
            "task_description": f"Author high-density comparison tables and authoritative FAQ citation assets for: '{directive_text}'.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/specs",
            "completion_time": "35m"
        })
        # Agent 5: Consensus Builder
        subtasks.append({
            "task_id": f"TSK-PR-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Chloe Martin (Agent 5: Consensus Builder)",
            "task_description": f"Coordinate technical benchmark distribution across Reddit, GitHub discussions, and tech forums.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://reddit.com/r/SaaS",
            "completion_time": "45m"
        })
        # Agent 4: Analyst
        subtasks.append({
            "task_id": f"TSK-ANA-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "David Chen (Agent 4: SoM Performance Analyst)",
            "task_description": f"Monitor post-distribution brand sentiment and evaluate Share of Model shift for new content.",
            "priority": "Medium",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/reports",
            "completion_time": "30m"
        })

    # Pattern: Technical, CMS, API, Website Integration Directive
    elif any(k in text_lower for k in ["tech", "code", "schema", "api", "cms", "wordpress", "webflow", "site", "hata", "fix"]):
        # Agent 6: Technical Auditor
        subtasks.append({
            "task_id": f"TSK-TECH-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Alex Rivera (Agent 6: Technical AEO Auditor)",
            "task_description": f"Audit technical infrastructure, inspect server headers, and generate code patches for: '{directive_text}'.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://github.com/ArdaTkn/aeo-agency/schema",
            "completion_time": "30m"
        })
        # Agent 7: Solution Engineer
        subtasks.append({
            "task_id": f"TSK-SOL-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Tariq Mansour (Agent 7: Solution Engineer)",
            "task_description": f"Deploy validated code payload to client CMS endpoints and verify webhook synchronization.",
            "priority": "High",
            "status": "Completed",
            "output_link": "https://api.clientdomain.com/webhooks",
            "completion_time": "25m"
        })

    # Default Balanced Delegation
    else:
        subtasks.append({
            "task_id": f"TSK-RES-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Marcus Vance (Agent 2: Lead LLM Researcher)",
            "task_description": f"Execute exploratory research and competitor benchmarking for: '{directive_text}'.",
            "priority": "Medium",
            "status": "Completed",
            "output_link": "Exploratory Audit Matrix",
            "completion_time": "30m"
        })
        subtasks.append({
            "task_id": f"TSK-KNOW-{int(time.time())}",
            "assigned_by": "Sarah Jenkins (PM)",
            "agent_name": "Elena Rostova (Agent 3: Knowledge Architect)",
            "task_description": f"Structure deliverables into machine-readable format for: '{directive_text}'.",
            "priority": "Medium",
            "status": "Completed",
            "output_link": "Structured Asset Staging",
            "completion_time": "35m"
        })

    return subtasks
