import random
class tools:
    def __init__(self):
        self.curr_ord = ""
        self.orders = ("ORD123", "ORD124", "ORD125")
        self.orders_status = [
            {"Order Number" : "ORD123" , "status": "in transit",  "tracking_number": "TRK123456", "estimated_delivery_date": "2025-10-10"},
            {"Order Number" : "ORD124", "status": "delivered", "tracking_number": "TRK123457", "delivery_date": "2025-02-03"},
            {"Order Number" : "ORD125", "status": "at warehouse", "tracking_number": "TRK123458", "estimated_delivery_date": "2025-12-12"},
        ]

    def get_order_details(self, email):
        """
        Fetches the order details from the system using the order number.

        Args:
            email (str): email of the customer.

        Returns:
            dict: Order details or an error message if not found.
        """
        self.curr_ord = random.choice(self.orders_status) if self.curr_ord == "" else self.curr_ord
        return {
                "status_code": 1,
                "message": f"Order successfully found : {self.curr_ord}"
            }

    def offer_discount_expedited_shipping(self, order_number):
        """
        Offers a discount on expedited shipping to the customer as a gesture of goodwill.

        Args:
            order_number (str): Order number of the customer.

        Returns:
            dict: Offer details or an error message if not found.
        """
        if order_number in self.orders:
            return {
                "status_code": 1,
                "message": "We can successfully offer a discount of 10 percent on expedite delivery charge making it just of 10$ and you can expect delivery in 2 days"
            }
        return {
            "status_code": 0,
            "message": "Order not found."
        }
    
    def transferToHuman(self):
        """
        Escalates the issue for further investigation.

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
        Marks the problem as resolved when customer is satisfied with the delivery resolution or accepts a discounted expedited shipping option. 
        Returns:
            dict: Resolution status or an error message if the account is not found.
        """
        # Check if the account exists
        return {
                "status_code": 1,
                "message": "The problem been successfully resolved. Thank you for using our services.",
            }
    
# Define tools as per the typical "agent tool" definition
tools_description = [
    {
        "type": "function",
        "conf": {
            "func_name": "get_order_details",
            "func_desc": "Use this tool to fetch the order details from the system using the order number.",
            "func_args": {
                "email": {
                    "type": "string",
                    "description": "Email of the customer.",
                },
            },
        },
        "required": ["email"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "offer_discount_expedited_shipping",
            "func_desc": "For orders still at the warehouse(not in transit) use this tool to offer a discount on expedited shipping",
            "func_args": {
                "order_number": {
                    "type": "string",
                    "description": "Order number of the customer gathered from the details internally. (Dont ask user for the oder number)",
                },
            },
        },
        "required": ["order_number"],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "transferToHuman",
            "func_desc": "Use this tool to escalate the issue for further investigation.",
            "func_args": {},
        },
        "required": [],
    },
    {
        "type": "function",
        "conf": {
            "func_name": "mark_problem_resolved",
            "func_desc": "Use tool mark_problem_resolved when customer is satisfied with the delivery resolution or accepts a discounted expedited shipping option",
            "func_args": {},
        },
        "required": [],
    }
]
