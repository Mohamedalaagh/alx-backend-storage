-- Creation a trigger that decreases the quantity
-- New & OLD are MySQL extensions to triggers
-- enable access to columns in the rows affected by a trigger

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
