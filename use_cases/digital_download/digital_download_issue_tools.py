import random 

class tools:
    def __init__(self):
        # Mock data for customer details
        self.customer_details = {
            "jane.doe@example.com": {
                "name": "Jane Doe",
                "customer_id": "CUST-12345",
                "credit_card_last_four_digits": "5666",
            }
        }

        # Mock data for purchase history
        self.purchase_history = {
            "jane.doe@example.com": [
                {
                    "purchase_id": "PUR-67890",
                    "product_name": "Digital Product A",
                    "purchase_date": "2023-10-01",
                    "transaction_id": "TXN-98765",
                },
                {
                    "purchase_id": "PUR-54321",
                    "product_name": "Digital Product B",
                    "purchase_date": "2023-10-05",
                    "transaction_id": "TXN-12345",
                },
                {
                    "purchase_id": "PUR-54222",
                    "product_name": "Digital Product C",
                    "purchase_date": "2023-10-10",
                    "transaction_id": "TXN-12346",
                },
            ]
        }

        # Mock data for download status
        self.download_status = {
            "PUR-67890": "error in download",
            "PUR-54321": "success",
            "PUR-54222" : "currently unavailable"
        }

    def get_customer_details(self, email, credit_card_last_four_digits):
        """
        Fetches the customer's details based on the provided email address.

        Args:
            email (str): Email address of the customer.
            credit_card_last_four_digits (str): Last four digits of the credit card.

        Returns:
            dict: Customer details or an error message if not found.
        """
        if email in self.customer_details:
            if self.customer_details[email].get("credit_card_last_four_digits") == credit_card_last_four_digits:
                return {
                    "status_code": 1,
                    "message": f"Customer details successfully found : {self.customer_details[email]}",
                }
            else:
                return {
                    "status_code": 0,
                    "message": f"Credit Card Mismatch, kindly check credit card details",
                }
        return {
            "status_code": 0,
            "message": "Customer details not found.",
        }

    def get_purchase_history(self, email):
        """
        Fetches the customer's purchase history.

        Args:
            email (str): Email address of the customer.

        Returns:
            list[dict]: Purchase history or an error message if not found.
        """
        if email in self.purchase_history:
            return {
                "status_code": 1,
                "message": f"Customer purchase history successfully found : {random.choice(self.purchase_history[email])}",
            }
        return {
            "status_code": 0,
            "message": "Purchase history not found with the provided email address.",
        }

    def get_download_status(self, purchase_id):
        """
        Fetches the download status of the reported purchase.

        Args:
            purchase_id (str): Purchase ID.

        Returns:
            dict: Download status or an error message if not found.
        """
        if purchase_id in self.download_status:
            return {
                "status_code": 1,
                "message": f"Download status successfully found : { self.download_status[purchase_id]}",
            }
        return {
            "status_code": 0,
            "message": "Download status not found for the given purchase id.",
        }

    def reset_download(self, purchase_id):
        """
        Resets the download for the reported purchase.

        Args:
            purchase_id (str): Purchase ID.

        Returns:
            dict: Reset status or an error message if not found.
        """
        if purchase_id in self.download_status:
            self.download_status[purchase_id] = "reset"
            return {
                "status_code": 1,
                "message": "Download reset successfully.",
            }
        return {
            "status_code": 0,
            "message": "Download reset failed.",
        }

    def transferToHuman(self):
        """
        Escalates the issue to the technical team for further investigation.

        Args:

        Returns:
            dict: Escalation status or an error message if not found.
        """
        return {
            "status_code": 1,
            "message": f"Issue escalated successfully.",
        }
    
    def mark_problem_resolved(self):
        """
        Marks the problem as resolved for the customer's account. Use this tool to mark the problem or issue is fixed.
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
            "func_name": "get_customer_details",
            "func_desc": "Fetches the customer's details based on the provided email address and verifies the last four digits of the credit card.",
            "func_args": {
                "email": {
                    "type": "string",
                    "description": "Email address of the customer.",
                },
                "credit_card_last_four_digits": {
                    "type": "string",
                    "description": "Last four digits of the credit card used for the purchase.",
                },
            },
        },
        "required": ["email", "credit_card_last_four_digits"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "get_purchase_history",
            "func_desc": "Fetches the customer's purchase history based on the provided email address.",
            "func_args": {
                "email": {
                    "type": "string",
                    "description": "Email address of the customer.",
                },
            },
        },
        "required": ["email"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "get_download_status",
            "func_desc": "Fetches the download status of the reported purchase using the purchase ID.",
            "func_args": {
                "purchase_id": {
                    "type": "string",
                    "description": "Purchase ID of the reported purchase, fetched from get_purchase_history tool.",
                },
            },
        },
        "required": ["purchase_id"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "reset_download",
            "func_desc": "Resets the download for the reported purchase using the purchase ID.",
            "func_args": {
                "purchase_id": {
                    "type": "string",
                    "description": "Purchase ID of the reported purchase, fetched from get_purchase_history tool.",
                },
            },
        },
        "required": ["purchase_id"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "transferToHuman",
            "func_desc": "Escalates the issue to the technical team for further investigation. Use this tool when the issue cannot be resolved automatically.",
            "func_args": {},
        },
        "required": [],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "mark_problem_resolved",
            "func_desc": "Use tool mark_problem_resolved when customer is able to download the product or decides to try again later, this marks the end of conversation",
            "func_args": {},
        },
        "required": [],
    }
]