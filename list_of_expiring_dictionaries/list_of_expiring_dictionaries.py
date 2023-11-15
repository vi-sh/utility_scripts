import time
class ExpiringDictList:

    def __init__(self):
        self.led = []
        self.expired_pool_ids = []
        self.active_pool_ids = []

    def __repr__(self):
        return f"{self.led}"

    def add_pool_id(self, pool_id, exp_time):
        if not self.led:
            print(f"Pool id {pool_id} does not exist - adding it")
            current_time = int(time.time())
            dict_data = {'pool_id': pool_id, 'exp_time': current_time + int(exp_time)}
            self.led.append(dict_data)
        else:
            for _pool in self.led:
                if pool_id in _pool:
                    print(f"Pool ID - {pool_id} already exist")
                else:
                    current_time = int(time.time())
                    print(f"Pool id {pool_id} does not exist - adding it")
                    dict_data = {'pool_id': pool_id, 'exp_time': current_time + int(exp_time)}
                    self.led.append(dict_data)
                    break

    def remove_expired_data(self):
        current_time = int(time.time())
        for item in self.led:
            if item['exp_time'] > current_time:
                if item['pool_id'] not in self.active_pool_ids:
                    self.active_pool_ids.append(item)
            else:
                print(f"Pool ID - {item['pool_id']} has expired")
                if item['pool_id'] not in self.expired_pool_ids:
                    self.expired_pool_ids.append(item)
                    self.led.pop(item)

        return self.active_pool_ids, self.expired_pool_ids

    def get_led(self):
        self.active_pool_ids, self.expired_pool_ids = self.remove_expired_data()
        print("Below are the active pool ids")
        print(self.active_pool_ids)

    def delete_pool_id(self, pool_id):
        self.led = [item for item in self.led if item['pool_id'] != pool_id]

    def reset_pool(self):
        del self.led, self.expired_pool_ids, self.active_pool_ids

# Example usage:
expiring_dict_list = ExpiringDictList()
