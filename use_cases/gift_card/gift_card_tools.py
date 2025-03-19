import random
class tools:
    def __init__(self):
        # Mock database for user accounts
        self.gitf_cards = {"rus@gmail.com" : ["GC-987654", "GC-123456", "GC-123458"]}

        # Mock database for gift cards
        self.gift_card_database = {
            "GC-987654": {
                "value": 50.0,
                "is_redeemed": False,
                "expired" : False
            },
            "GC-123456": {
                "value": 100.0,
                "is_redeemed": True,
                "expired" : False
            },
            "GC-123458": {
                "value": 80.0,
                "is_redeemed": False,
                "expired" : True
            }
        }

    def fetch_gift_card(self, email):
        """
        Retrieves the user's gift card details using email.

        Args:
            email

        Returns:
            dict: User account details or an error message if not found.
        """
        if email in self.gitf_cards:
            return {
                "status_code": 1,
                "message": f"Gift card sucessfully found with asssociated email : {random.choice(list(self.gitf_cards[email]))}",
            }
        return {
            "status_code": 0,
            "message": "Incorrect email"
        }

    def get_gift_card_details(self, gift_card_code):
        """
        Retrieves the details of a specific gift card using its code.

        Args:
            gift_card_code (str): The gift card code provided by the customer.

        Returns:
            dict: Gift card details or an error message if not found.
        """
        if gift_card_code in self.gift_card_database:
            return {
                "status_code": 1,
                "message": f"Gift card details retrieved successfully. Details Value = {self.gift_card_database[gift_card_code]['value']}, expired = {self.gift_card_database[gift_card_code]['expired']}"
            }
        return {
            "status_code": 0,
            "message": "Gift card not found."
        }

    def check_gift_card_redeemed(self, gift_card_code):
        """
        Checks if the gift card has already been redeemed.

        Args:
            gift_card_code (str): The gift card code provided by the customer.

        Returns:
            dict: Redemption status of the gift card.
        """
        if gift_card_code in self.gift_card_database:
            is_redeemed = self.gift_card_database[gift_card_code]["is_redeemed"]
            return {
                "status_code": 1,
                "message": str(is_redeemed)
            }
        return {
            "status_code": 0,
            "message": "Gift card not found."
        }

    def apply_gift_card_to_account(self, gift_card_code):
        """
        Applies the gift card to the user's account.

        Args:
            gift_card_code (str): The gift card code provided by the customer.

        Returns:
            dict: Application status of the gift card.
        """
        return {
                    "status_code": 1,
                    "message": "Gift card successfully applied to the account."
                }

    def transferToHuman(self):
        """
        Use this tool to escalate and transfer to human if the gift card is redeemed or expired and customer has further issues or is not satisfied. 

        Returns:
            dict: Escalation status.
        """
        return {
            "status_code": 1,
            "message": "Issue successfully escalated to a human agent."
        }
    
    def mark_problem_resolved(self):
        """
        Use this tool to end conversation if the gift card is not usable and customer has no further issues. 
        Returns:
            dict: Resolution status or an error message if the account is not found.
        """
        # Check if the account exists
        return {
                "status_code": 1,
                "message": "The problem been successfully resolved. Thank you for using our services.",
            }
    
tools_description = [
    {
        "type": "function",
        "conf": {
            "func_name": "fetch_gift_card",
            "func_desc": "Use this tool to retrieve the user's gift card code using their email.",
            "func_args": {
                "email": {
                    "type": "string",
                    "description": "User's email address",
                },
            },
        },
        "required": ["email"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "get_gift_card_details",
            "func_desc": "Use this tool to gather the details like gift card value and if its expired using gift card code. (Dont ask user for the code fetch it)",
            "func_args": {
                "gift_card_code": {
                    "type": "string",
                    "description": "The gift card code fetched before (Dont ask user for the code fetch it)",
                },
            },
        },
        "required": ["gift_card_code"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "check_gift_card_redeemed",
            "func_desc": "Use this tool to check if the gift card has already been redeemed before applying it manually. it returns True is the card is redeemed and False otherwise",
            "func_args": {
                "gift_card_code": {
                    "type": "string",
                    "description": "The gift card code provided by the customer.",
                },
            },
        },
        "required": ["gift_card_code"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "apply_gift_card_to_account",
            "func_desc": "Use this tool to apply a valid and not redeemed gift card to the user's account.",
            "func_args": {
                "gift_card_code": {
                    "type": "string",
                    "description": "The gift card code provided by the customer.",
                },
            },
        },
        "required": ["gift_card_code"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "transferToHuman",
            "func_desc": "Use this tool to escalate the issue to a human agent for further assistance.",
            "func_args": {},
        },
        "required": [],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "mark_problem_resolved",
            "func_desc": "Use this tool when the gift card is unusable and if customer has no further issues at this time. This tool markes the end of the conversation",
            "func_args": {},
        },
        "required": [],
        "return_directly": True
    }
]