def create_workflow_transition(workflow_transitions_data: List[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Create workflow transitions with flexible configuration
    
    Example Data Structures:
    
    # Single Workflow Transition Configuration
    single_workflow_transition = {
        "state": "Draft",                     # Current state
        "action": "Submit",                   # Action to perform
        "next_state": "Pending Approval",     # State to transition to
        "allowed": "Requestor",               # Role allowed to perform action
        
        # Optional additional fields
        "condition": "",                      # Optional condition for transition
        "allow_self_approval": 0,             # Flag for self-approval
        "description": "Submit draft for approval" # Optional description
    }
    
    # Multiple Workflow Transitions Configuration
    multiple_workflow_transitions = [
        {
            "state": "Draft",
            "action": "Submit",
            "next_state": "Pending Approval",
            "allowed": "Requestor"
        },
        {
            "state": "Pending Approval",
            "action": "Approve",
            "next_state": "Approved",
            "allowed": "Approver"
        },
        {
            "state": "Pending Approval",
            "action": "Reject",
            "next_state": "Rejected",
            "allowed": "Approver"
        }
    ]
    
    # Complex Workflow Transitions with Multiple Scenarios
    complex_workflow_transitions = [
        {
            "state": "Draft",
            "action": "Submit for Technical Evaluation",
            "next_state": "Technical Evaluation",
            "allowed": "Initiator",
            "condition": "document.total_value > 100000"
        },
        {
            "state": "Technical Evaluation",
            "action": "Recommend",
            "next_state": "Commercial Evaluation",
            "allowed": "Technical Committee"
        },
        {
            "state": "Commercial Evaluation",
            "action": "Approve",
            "next_state": "Final Approval",
            "allowed": "Finance Manager",
            "condition": "document.recommended_value <= budget"
        }
    ]
    
    # Purchase Workflow Transitions Example
    purchase_workflow_transitions = [
        {
            "state": "Draft",
            "action": "Submit",
            "next_state": "Pending Technical Evaluation",
            "allowed": "Procurement Officer"
        },
        {
            "state": "Pending Technical Evaluation",
            "action": "Technical Review",
            "next_state": "Technical Evaluated",
            "allowed": "Technical Committee"
        },
        {
            "state": "Technical Evaluated",
            "action": "Submit for Commercial",
            "next_state": "Pending Commercial Evaluation",
            "allowed": "Procurement Officer"
        },
        {
            "state": "Pending Commercial Evaluation",
            "action": "Commercial Review",
            "next_state": "Commercially Evaluated",
            "allowed": "Finance Committee"
        },
        {
            "state": "Commercially Evaluated",
            "action": "Approve",
            "next_state": "Approved",
            "allowed": "Managing Director"
        },
        {
            "state": "Draft",
            "action": "Cancel",
            "next_state": "Cancelled",
            "allowed": "Procurement Officer"
        }
    ]
    
    Args:
        workflow_transitions_data (List[Dict], optional): List of workflow transition configurations
    
    Returns:
        Dict containing creation details
    """
    try:
        # If no data provided, use default method
        if workflow_transitions_data is None:
            workflow_transitions_data = _get_default_workflow_transitions()
        
        created_transitions = []
        existing_transitions = []
        error_transitions = []
        
        for transition in workflow_transitions_data:
            # Validate required fields
            if not all(key in transition for key in ['state', 'action', 'next_state', 'allowed']):
                error_transitions.append({
                    "error": "Missing required fields",
                    "transition": transition
                })
                continue
            
            # Unique identifier for transition
            transition_key = (
                transition['state'], 
                transition['action'], 
                transition['next_state']
            )
            
            # Check if transition exists
            existing = frappe.db.exists("Workflow Transition", {
                "state": transition['state'],
                "action": transition['action'],
                "next_state": transition['next_state']
            })
            
            if existing:
                existing_transitions.append(transition_key)
                continue
            
            try:
                # Create workflow transition
                workflow_transition = frappe.get_doc({
                    "doctype": "Workflow Transition",
                    "state": transition['state'],
                    "action": transition['action'],
                    "next_state": transition['next_state'],
                    "allowed": transition['allowed'],
                    
                    # Optional fields
                    "condition": transition.get('condition', ''),
                    "allow_self_approval": transition.get('allow_self_approval', 0)
                })
                
                workflow_transition.insert(ignore_permissions=True)
                created_transitions.append(transition_key)
            
            except Exception as transition_error:
                error_transitions.append({
                    "transition": transition_key,
                    "error": str(transition_error)
                })
        
        # Commit changes
        frappe.db.commit()
        
        return {
            "status": "success",
            "created_transitions": created_transitions,
            "existing_transitions": existing_transitions,
            "error_transitions": error_transitions
        }
    
    except Exception as e:
        frappe.log_error(f"Workflow Transition Creation Error: {str(e)}")
        return {
            "status": "error",
            "message": str(e)
        }

# Example usage function
def workflow_transition_setup_example():
    """
    Example of creating workflow transitions
    """
    # Purchase Workflow Transitions
    purchase_workflow_transitions = [
        {
            "state": "Draft",
            "action": "Submit",
            "next_state": "Pending Technical Evaluation",
            "allowed": "Procurement Officer"
        },
        {
            "state": "Pending Technical Evaluation",
            "action": "Technical Review",
            "next_state": "Technical Evaluated",
            "allowed": "Technical Committee"
        }
        # ... other transitions
    ]
    
    # Create workflow transitions
    result = create_workflow_transition(purchase_workflow_transitions)
    return result

# Whitelisted method for API access
@frappe.whitelist()
def setup_workflow_transitions(workflow_transitions=None):
    """
    Publicly accessible method to create workflow transitions
    """
    return create_workflow_transition(workflow_transitions)