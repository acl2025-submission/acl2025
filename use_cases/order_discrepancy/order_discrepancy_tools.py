import random

class tools:
    def __init__(self):
        self.orders = {
            "ORD-12345": {
                "customer_name": "Jane Doe",
                "email": "jane.doe@example.com"
            }
        }

        self.check_item = None

    def verify_customer_identity(self, email, order_number):
        """
        Verifies the customer's identity by comparing the provided name and email address with the ones in the order details.

        Args:
            eamil (str): email address provided by the customer.
            order_number (dict): Order details fetched from the system.

        Returns:
            dict: Verification status or an error message if not matched.
        """
        if (self.orders[order_number]["email"] == email):
            return {
                "status_code": 1,
                "message": "Customer identity verified successfully.",
            }
        return {
            "status_code": 0,
            "message": "Customer identity verification failed.",
        }

    def check_item_in_order(self, item, order_number):
        """
        Checks if the described item is included in the original order.

        Args:
            item (str): Product A/B etc.
            order_number (dict): Order number provided by the user.

        Returns:
            dict: Inclusion status or an error message if not found.
        """
        if order_number not in self.orders:
            return {
                "status_code": 0,
                "message": "Order number not found.",
            }
        else:
            if self.check_item is None:
                self.check_item = random.choice([
                    {
                        "status_code": 1,
                        "message": "Item was included in the order.",
                    },
                    {
                        "status_code": 0,
                        "message": "Item was not included in the order.",
                    },
                ])
            return self.check_item

    def initiate_shipping_request(self, item_name):
        """
        Initiates a new shipping request for the missing item.

        Args:
            item (str): Missing item provided by the customer.

        Returns:
            dict: Shipping confirmation or an error message if not initiated.
        """
        return {
            "status_code": 1,
            "message": f"Shipping request successfully initiated for {item_name}. Tracking number: SHIP-12345, which will also be sent on email.",
        }

    def place_new_order(self, item_name):
        """
        Places a new order for the missing item.

        Args:
            item (str): Missing item provided by the customer.

        Returns:
            dict: New order confirmation.
        """
        return {
            "status_code": 1,
            "message": f"New order successfully placed for {item_name}. Confirmation number: ORD-67890",
        }

    def transferToHuman(self):
        """
        Escalates the issue to the team for further investigation.

        Args:

        Returns:
            dict: Escalation status or an error message if not found.
        """
        return {
            "status_code": 1,
            "message": "Issue escalated successfully.",
        }
    def mark_problem_resolved(self):
        """
        Marks the problem as resolved when customer is satisfied with the delivery resolution or accepts a discounted expedited shipping option. 
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
            "func_name": "verify_customer_identity",
            "func_desc": "Verifies the customer's identity by comparing the provided email with the ones in the order details.",
            "func_args": {
                "email": {
                    "type": "string",
                    "description": "Email address provided by the customer.",
                },
                "order_number": {
                    "type": "string",
                    "description": "Order number provided by the customer.",
                },
            },
        },
        "required": ["email", "order_number"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "check_item_in_order",
            "func_desc": "Checks if the described item is included in the original order.",
            "func_args": {
                "item": {
                    "type": "string",
                    "description": "Name of the item to check (e.g., Product A, Product B).",
                },
                "order_number": {
                    "type": "string",
                    "description": "Order number provided by the customer.",
                },
            },
        },
        "required": ["item", "order_number"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "initiate_shipping_request",
            "func_desc": "Use this tool to initiate a shipping request for the missing item.",
            "func_args": {
                "item_name": {
                    "type": "string",
                    "description": "Name of the missing item.",
                },
            },
        },
        "required": ["item"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "place_new_order",
            "func_desc": "Use this tool to Place a new order for the missing item if it was not part of the original order.",
            "func_args": {
                "item_name": {
                    "type": "string",
                    "description": "Name of the missing item.",
                },
            },
        },
        "required": ["item"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "transferToHuman",
            "func_desc": "Escalates the issue to the technical team for further investigation. Use this tool when the issue cannot be resolved automatically. or conversation goes out of scope",
            "func_args": {},
        },
        "required": [],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "mark_problem_resolved",
            "func_desc": "Use tool mark_problem_resolved when customer is satisfied with the resolution or places a new order",
            "func_args": {},
        },
        "required": [],
    }
]