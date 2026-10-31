raw_devices = [
{"device_code": "D301", "type": "laptop",
"price": 18500000, "status": "in_stock"},
{"device_code":"d101 ", "type": "phone",
"price": 6900000, "status": "in_stock"},
{"device_code": "D202", "type": "tablet",
"price": 9500000, "status": "out_of_stock"},
{"device_code": "D102", "type": "phone",
"price": 4200000, "status": "discontinued"},
{"device_code": "D302", "type": "laptop",
"price": 22000000, "status": "in_stock"}
]


def clean_and_validate_devices(raw_device):
    valid = []
    for d in raw_device:
        code = d.get("device_code").strip().upper()
        if d.startswith("D") and code[1:].isdigit():
            d["device_code"] = code
            valid.append(d)
    return valid
    
def search_devices(raw_device,price,status):
    result = []
    for d in raw_device:
        if d["status"] == status and d["price"] == price:
            result.append(d)
    return result

def sort_devices_by_price_desc(raw_device):
    n = len(raw_device)
    for i in range(n):
        for j in range(0,n-i-1):
            if raw_device[i]["price"] < raw_device[j+1]["price"]:
                raw_device[j],raw_device[j+1] = raw_device[j+1],raw_device[j]
                return raw_device