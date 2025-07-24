import frappe

def create_simple_workflow():
    if frappe.db.exists("Workflow", "Simple Bid Workflow"):
        return

    # Create Workflow States
    for state in ["Draft", "Review", "Approved"]:
        if not frappe.db.exists("Workflow State", state):
            frappe.get_doc({
                "doctype": "Workflow State",
                "workflow_state_name": state,
                "style": "Primary" if state == "Draft" else ("Success" if state == "Approved" else "Info")
            }).insert(ignore_permissions=True)
            print(f"Created Workflow State: {state}")

    # Create Workflow Actions
    actions = ["Send for Review", "Approve", "Reject"]
    for action in actions:
        if not frappe.db.exists("Workflow Action Master", action):
            frappe.get_doc({
                "doctype": "Workflow Action Master",
                "workflow_action_name": action
            }).insert(ignore_permissions=True)
            print(f"Created Workflow Action: {action}")

    # Create the Workflow
    if not frappe.db.exists("Workflow", "Simple Bid Workflow"):
        workflow = frappe.get_doc({
            "doctype": "Workflow",
            "workflow_name": "Simple Bid Workflow",
            "document_type": "Bid Document",
            "is_active": 1,
            "workflow_state_field": "workflow_state",
            "states": [
                {
                    "state": "Draft",
                    "doc_status": "0",
                    "allow_edit": "All"
                },
                {
                    "state": "Review", 
                    "doc_status": "0",
                    "allow_edit": "All"
                },
                {
                    "state": "Approved",
                    "doc_status": "1",
                    "allow_edit": "All"
                }
            ],
            "transitions": [
                {
                    "state": "Draft",
                    "action": "Send for Review",
                    "next_state": "Review",
                    "allowed": "All"
                },
                {
                    "state": "Review",
                    "action": "Approve",
                    "next_state": "Approved", 
                    "allowed": "All"
                },
                {
                    "state": "Review",
                    "action": "Reject",
                    "next_state": "Draft",
                    "allowed": "All"
                }
            ]
        })
        workflow.insert(ignore_permissions=True)
        print("Workflow created: Simple Bid Workflow")
        
        # Update the name to match workflow_name for UI visibility
        frappe.db.set_value("Workflow", workflow.name, "name", "Simple Bid Workflow")
        frappe.db.commit()
        print("Updated workflow name for UI visibility")
        
        # Clear cache to ensure it appears in the UI
        frappe.clear_cache()
        frappe.cache().delete_value("workflow_" + "Bid Document")
        frappe.clear_document_cache("Workflow", "Simple Bid Workflow")
        print("Cache cleared")




############## TO CREATE WORKFLOW USING THIS SCRIPT ####################
# bench --site yoursite console
# In [1]: from cerp.procurement_module.setup.create_workflows import
#    ...: create_simple_workflow
#
# In [2]: create_simple_workflow()
# Workflow created: Simple Bid Workflow
# Updated workflow name for UI visibility
# Cache cleared
#
# In [3]:





























import frappe

def create_workflow_states(states_config):
    """
    Create workflow states from configuration
    
    Args:
        states_config: List of dicts with state info
        Example: [{"name": "Draft", "style": "Primary"}, ...]
    
    Returns:
        list: Created state names
    """
    created_states = []
    
    for state_config in states_config:
        state_name = state_config["name"]
        
        if not frappe.db.exists("Workflow State", state_name):
            frappe.get_doc({
                "doctype": "Workflow State",
                "workflow_state_name": state_name,
                "style": state_config.get("style", "Primary")
            }).insert(ignore_permissions=True)
            created_states.append(state_name)
            print(f"✓ Created Workflow State: {state_name}")
        else:
            print(f"→ Workflow State already exists: {state_name}")
    
    return created_states


def create_workflow_actions(actions_list):
    """
    Create workflow actions
    
    Args:
        actions_list: List of action names
        Example: ["Send for Review", "Approve", "Reject"]
    
    Returns:
        list: Created action names
    """
    created_actions = []
    
    for action in actions_list:
        if not frappe.db.exists("Workflow Action Master", action):
            frappe.get_doc({
                "doctype": "Workflow Action Master",
                "workflow_action_name": action
            }).insert(ignore_permissions=True)
            created_actions.append(action)
            print(f"✓ Created Workflow Action: {action}")
        else:
            print(f"→ Workflow Action already exists: {action}")
    
    return created_actions


def create_workflow_roles(roles_list):
    """
    Create roles if they don't exist
    
    Args:
        roles_list: List of role names
        Example: ["Bid Manager", "Bid Reviewer"]
    
    Returns:
        list: Created role names
    """
    created_roles = []
    
    for role in roles_list:
        if not frappe.db.exists("Role", role):
            frappe.get_doc({
                "doctype": "Role",
                "role_name": role,
                "desk_access": 1
            }).insert(ignore_permissions=True)
            created_roles.append(role)
            print(f"✓ Created Role: {role}")
        else:
            print(f"→ Role already exists: {role}")
    
    return created_roles


def add_workflow_field_to_doctype(doctype_name, field_name="workflow_state"):
    """
    Add workflow state field to doctype if it doesn't exist
    
    Args:
        doctype_name: Name of the doctype
        field_name: Name of the workflow field (default: workflow_state)
    
    Returns:
        bool: True if field was added, False if already exists
    """
    meta = frappe.get_meta(doctype_name)
    has_field = any(field.fieldname == field_name for field in meta.fields)
    
    if not has_field:
        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": doctype_name,
            "label": "Workflow State",
            "fieldname": field_name,
            "fieldtype": "Link",
            "options": "Workflow State",
            "hidden": 1,
            "allow_on_submit": 1,
            "no_copy": 1
        }).insert()
        print(f"✓ Added {field_name} field to {doctype_name}")
        return True
    else:
        print(f"→ {field_name} field already exists in {doctype_name}")
        return False


def build_workflow_states(states_config):
    """
    Build states list for workflow document
    
    Args:
        states_config: List of state configurations
    
    Returns:
        list: Formatted states for workflow
    """
    return [
        {
            "state": state["name"],
            "doc_status": state.get("doc_status", "0"),
            "allow_edit": state.get("allow_edit", "All"),
            "is_optional_state": state.get("is_optional", 0)
        }
        for state in states_config
    ]


def build_workflow_transitions(transitions_config):
    """
    Build transitions list for workflow document
    
    Args:
        transitions_config: List of transition configurations
    
    Returns:
        list: Formatted transitions for workflow
    """
    return [
        {
            "state": trans["from_state"],
            "action": trans["action"],
            "next_state": trans["to_state"],
            "allowed": trans.get("allowed", "All"),
            "allow_self_approval": trans.get("allow_self_approval", 1)
        }
        for trans in transitions_config
    ]


def create_workflow_document(workflow_config):
    """
    Create the actual workflow document
    
    Args:
        workflow_config: Dictionary with workflow configuration
    
    Returns:
        Document: Created workflow document
    """
    workflow = frappe.get_doc({
        "doctype": "Workflow",
        "workflow_name": workflow_config["name"],
        "document_type": workflow_config["document_type"],
        "is_active": workflow_config.get("is_active", 1),
        "workflow_state_field": workflow_config.get("state_field", "workflow_state"),
        "send_email_alert": workflow_config.get("send_email_alert", 0),
        "states": workflow_config["states"],
        "transitions": workflow_config["transitions"]
    })
    
    workflow.insert(ignore_permissions=True)
    
    # Update name for UI visibility
    frappe.db.set_value("Workflow", workflow.name, "name", workflow_config["name"])
    frappe.db.commit()
    
    return workflow


def clear_workflow_cache(document_type):
    """
    Clear cache after workflow creation
    
    Args:
        document_type: The document type for which workflow was created
    """
    frappe.clear_cache()
    frappe.cache().delete_value(f"workflow_{document_type}")
    print("✓ Cache cleared")


def get_simple_bid_workflow_config():
    """
    Get configuration for Simple Bid Workflow
    
    Returns:
        dict: Complete workflow configuration
    """
    return {
        "name": "Simple Bid Workflow",
        "document_type": "Bid Document",
        "is_active": 1,
        "state_field": "workflow_state",
        "states": [
            {"name": "Draft", "style": "Primary", "doc_status": "0", "allow_edit": "All"},
            {"name": "Review", "style": "Info", "doc_status": "0", "allow_edit": "All"},
            {"name": "Approved", "style": "Success", "doc_status": "1", "allow_edit": "All"}
        ],
        "transitions": [
            {
                "from_state": "Draft",
                "action": "Send for Review",
                "to_state": "Review",
                "allowed": "All"
            },
            {
                "from_state": "Review",
                "action": "Approve",
                "to_state": "Approved",
                "allowed": "All"
            },
            {
                "from_state": "Review",
                "action": "Reject",
                "to_state": "Draft",
                "allowed": "All"
            }
        ],
        "actions": ["Send for Review", "Approve", "Reject"],
        "roles": []  # Add specific roles if needed
    }


def create_simple_workflow():
    """
    Main function to create Simple Bid Workflow
    Uses individual functions for each operation
    """
    workflow_config = get_simple_bid_workflow_config()
    
    # Check if workflow already exists
    if frappe.db.exists("Workflow", workflow_config["name"]):
        print(f"→ Workflow already exists: {workflow_config['name']}")
        return
    
    try:
        print(f"\n🚀 Creating workflow: {workflow_config['name']}")
        
        # Step 1: Create workflow states
        print("\n📋 Creating Workflow States...")
        create_workflow_states(workflow_config["states"])
        
        # Step 2: Create workflow actions
        print("\n⚡ Creating Workflow Actions...")
        create_workflow_actions(workflow_config["actions"])
        
        # Step 3: Create roles if specified
        if workflow_config.get("roles"):
            print("\n👥 Creating Roles...")
            create_workflow_roles(workflow_config["roles"])
        
        # Step 4: Add workflow field to doctype
        print("\n🔧 Checking DocType Field...")
        add_workflow_field_to_doctype(
            workflow_config["document_type"], 
            workflow_config["state_field"]
        )
        
        # Step 5: Build workflow configuration
        workflow_states = build_workflow_states(workflow_config["states"])
        workflow_transitions = build_workflow_transitions(workflow_config["transitions"])
        
        # Step 6: Create the workflow
        print("\n📄 Creating Workflow Document...")
        workflow_doc_config = {
            "name": workflow_config["name"],
            "document_type": workflow_config["document_type"],
            "is_active": workflow_config["is_active"],
            "state_field": workflow_config["state_field"],
            "states": workflow_states,
            "transitions": workflow_transitions
        }
        
        workflow = create_workflow_document(workflow_doc_config)
        print(f"✓ Workflow created: {workflow.workflow_name}")
        
        # Step 7: Clear cache
        clear_workflow_cache(workflow_config["document_type"])
        
        print(f"\n✅ Successfully created workflow: {workflow_config['name']}")
        
    except Exception as e:
        print(f"\n❌ Error creating workflow: {str(e)}")
        frappe.db.rollback()
        raise


# Additional utility functions

def delete_workflow(workflow_name):
    """
    Delete a workflow and optionally its components
    
    Args:
        workflow_name: Name of the workflow to delete
    """
    if frappe.db.exists("Workflow", workflow_name):
        frappe.delete_doc("Workflow", workflow_name, force=True)
        frappe.db.commit()
        print(f"✓ Deleted workflow: {workflow_name}")
    else:
        print(f"→ Workflow not found: {workflow_name}")


def validate_workflow_config(config):
    """
    Validate workflow configuration before creation
    
    Args:
        config: Workflow configuration dictionary
    
    Returns:
        tuple: (is_valid, error_message)
    """
    required_fields = ["name", "document_type", "states", "transitions"]
    
    for field in required_fields:
        if field not in config:
            return False, f"Missing required field: {field}"
    
    if not config["states"]:
        return False, "At least one state is required"
    
    if not config["transitions"]:
        return False, "At least one transition is required"
    
    return True, None


############## TO CREATE WORKFLOW USING THIS SCRIPT ####################
# bench --site yoursite console
# In [1]: from cerp.procurement_module.setup.create_workflows import create_simple_workflow
#
# In [2]: create_simple_workflow()
# 
# 🚀 Creating workflow: Simple Bid Workflow
# 
# 📋 Creating Workflow States...
# ✓ Created Workflow State: Draft
# ✓ Created Workflow State: Review
# ✓ Created Workflow State: Approved
# 
# ⚡ Creating Workflow Actions...
# ✓ Created Workflow Action: Send for Review
# ✓ Created Workflow Action: Approve
# ✓ Created Workflow Action: Reject
# 
# 🔧 Checking DocType Field...
# → workflow_state field already exists in Bid Document
# 
# 📄 Creating Workflow Document...
# ✓ Workflow created: Simple Bid Workflow
# ✓ Cache cleared
# 
# ✅ Successfully created workflow: Simple Bid Workflow
#
# In [3]: 

# Example: Creating a custom workflow with roles
# """
# custom_config = {
#     "name": "Purchase Approval Workflow",
#     "document_type": "Purchase Order",
#     "is_active": 1,
#     "state_field": "workflow_state",
#     "states": [
#         {"name": "Draft", "style": "Primary", "doc_status": "0", "allow_edit": "Purchase User"},
#         {"name": "Pending Approval", "style": "Warning", "doc_status": "0", "allow_edit": "Purchase Manager"},
#         {"name": "Approved", "style": "Success", "doc_status": "1", "allow_edit": "System Manager"}
#     ],
#     "transitions": [
#         {
#             "from_state": "Draft",
#             "action": "Submit for Approval",
#             "to_state": "Pending Approval",
#             "allowed": "Purchase User"
#         },
#         {
#             "from_state": "Pending Approval",
#             "action": "Approve",
#             "to_state": "Approved",
#             "allowed": "Purchase Manager"
#         }
#     ],
#     "actions": ["Submit for Approval", "Approve"],
#     "roles": ["Purchase User", "Purchase Manager"]
# }

# # Create the custom workflow
# create_workflow_from_config(custom_config)
# """