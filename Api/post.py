import requests

payload = {
    "automation": True,
    "orders": [
        {
            "channel_id": "manual",
            "channel_order_id": "-BG2dAmouX25",
            "order_amount": 100,
            "paymentType": "COD",
            "billing_address": {
                "city": "New York",
                "name": "Yash Sharma",
                "email": "saurabhsinha209@gmail.com",
                "msisdn": "8377086507",
                "country": "India",
                "pinCode": 141006,
                "address1": "Baker Street",
                "address2": " ",
                "province": "Uttar Pradesh",
                "last_name": "Sharma",
                "first_name": "Yash"
            },
            "shipping_address": {
                "city": "New York",
                "name": "Yash Sharma",
                "email": "yash@growsimplee.com",
                "msisdn": "8377086507",
                "country": "India",
                "pinCode": 141006,
                "address1": "Baker Street",
                "address2": " ",
                "province": "Uttar Pradesh",
                "last_name": "Sharma",
                "first_name": "Yash"
            },
            "suborders": [
                {
                    "channel_listing_id": "CH1712",
                    "length": 10,
                    "breadth": 20,
                    "height": 90,
                    "dead_weight": 12,
                    "channel_suborder_id": "Abc",
                    "quantity": 1,
                    "codAmount": "10",
                    "suborder_value": "200",
                    "items": [
                        {
                            "name": "SONY XB10",
                            "description": "Mini Speaker",
                            "quantity": 3,
                            "item_id": "123456",
                            "item_value": "10.00"
                        }
                    ]
                }
            ]
        }
    ]
}

create = requests.post('https://oyvm2iv4xj.execute-api.ap-south-1.amazonaws.com/v1/orin/api/orders/',data=payload)
print(create)

