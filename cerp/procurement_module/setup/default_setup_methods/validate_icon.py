import frappe
from typing import List, Dict, Union, Any

# Comprehensive list of valid icons
VALID_WORKFLOW_ICONS = [
    "", "glass", "music", "search", "envelope", "heart", "star", "star-empty", 
    "user", "film", "th-large", "th", "th-list", "ok", "remove", "zoom-in", 
    "zoom-out", "off", "signal", "cog", "trash", "home", "file", "time", 
    "road", "download-alt", "download", "upload", "inbox", "play-circle", 
    "repeat", "refresh", "list-alt", "lock", "flag", "headphones", "volume-off", 
    "volume-down", "volume-up", "qrcode", "barcode", "tag", "tags", "book", 
    "bookmark", "print", "camera", "font", "bold", "italic", "text-height", 
    "text-width", "align-left", "align-center", "align-right", "align-justify", 
    "list", "indent-left", "indent-right", "facetime-video", "picture", "pencil", 
    "map-marker", "adjust", "tint", "edit", "share", "check", "move", 
    "step-backward", "fast-backward", "backward", "play", "pause", "stop", 
    "forward", "fast-forward", "step-forward", "eject", "chevron-left", 
    "chevron-right", "plus-sign", "minus-sign", "remove-sign", "ok-sign", 
    "question-sign", "info-sign", "screenshot", "remove-circle", "ok-circle", 
    "ban-circle", "arrow-left", "arrow-right", "arrow-up", "arrow-down", 
    "share-alt", "resize-full", "resize-small", "plus", "minus", "asterisk", 
    "exclamation-sign", "gift", "leaf", "fire", "eye-open", "eye-close", 
    "warning-sign", "plane", "calendar", "random", "comment", "magnet", 
    "chevron-up", "chevron-down", "retweet", "shopping-cart", "folder-close", 
    "folder-open", "resize-vertical", "resize-horizontal", "hdd", "bullhorn", 
    "bell", "certificate", "thumbs-up", "thumbs-down", "hand-right", "hand-left", 
    "hand-up", "hand-down", "circle-arrow-right", "circle-arrow-left", 
    "circle-arrow-up", "circle-arrow-down", "globe", "wrench", "tasks", "filter", 
    "briefcase", "fullscreen"
]

def validate_workflow_icon(icon: str) -> str:
    """
    Validate and clean workflow icon
    
    Args:
        icon (str): Icon to validate
    
    Returns:
        str: Validated icon or empty string
    """
    # If icon is None or not a string, return empty string
    if not isinstance(icon, str):
        return "globe"
    
    # Clean and normalize the icon
    icon = icon.strip().lower()
    
    # Check if icon is valid, return icon or empty string
    return icon if icon in VALID_WORKFLOW_ICONS else "globe"









# def create_bid_document_workflow():
#     """
#     Comprehensive method to create Bid Document Workflow
#     """
#     try:
#         # Prepare workflow data (from your existing method)
#         workflow_data = prepare_bid_document_workflow_data()
        
#         # Create workflow states with robust error handling
#         states_result = create_workflow_state(workflow_data['Workflow State'])
        
#         # Handle different scenarios
#         if states_result['status'] == 'error':
#             return {
#                 "status": "error",
#                 "message": "Failed to create workflow states",
#                 "details": states_result
#             }
        
#         # Continue with other workflow components if states are created successfully
#         # Create roles, transitions, etc.
#         roles_result = create_role(workflow_data['Role'])
#         transitions_result = create_workflow_transition(workflow_data['Workflow Transition'])
#         workflow_result = create_workflow(workflow_data['Workflow'][0])
        
#         return {
#             "status": "success",
#             "workflow_states": states_result,
#             "roles": roles_result,
#             "transitions": transitions_result,
#             "workflow": workflow_result
#         }
    
#     except Exception as e:
#         # Capture and log any unexpected errors
#         frappe.log_error(
#             title="Bid Document Workflow Setup Error",
#             message=str(e)
#         )
#         return {
#             "status": "error", 
#             "message": str(e)
#         }
