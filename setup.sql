-- Create table(s)

CREATE TABLE task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  summary VARCHAR(128),
  description TEXT,
  is_active BOOLEAN DEFAULT 1
);

--INSERT dummy data
INSERT INTO task (
  summary, 
  description
) VALUES (
  "Take out the trash",
  "Sort trash and take it out to the bins on the street"
);

INSERT INTO task (
  summary,
  description
) VALUES (
  "Buy groceries",
  "One pound of beef, potatoes, Idk, groceries"
);

INSERT INTO task (
  summary, 
  description
) VALUES (
  "Pick up dog",
  "Pick up dog from day care"
);
