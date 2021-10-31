class Paint:
    def __init__(self, bucket, color):
        self.color = color
        self.bucket = bucket
    def total_price(self):
        if self.color == 'white':
            return self.bucket * 1.99
        else:
            return self.bucket * 2.19

class DiscountedPaint(Paint):
    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discount = price * discount_percentage / 100
        return price - discount

price = DiscountedPaint(3, 'white')
print(price.discounted_price(20))
