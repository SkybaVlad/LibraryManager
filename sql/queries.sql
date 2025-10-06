-- 1. See all data about books
SELECT * FROM books

-- 2. See author and his book
SELECT 
  author.first_name,
  author.last_name,
  books.book_name
FROM
  author
INNER JOIN
  books
ON 
  author.author_id = books.author_id

-- 3. Count books on author
SELECT 
  author.first_name,
  author.last_name,
  COUNT(*) AS written_books
FROM 
  author
INNER JOIN 
  books
ON 
  author.author_id = books.author_id
GROUP BY
  author.first_name,
  author.last_name

-- 4. List of users that takes a books
SELECT 
	users.user_name,
	books.book_name
FROM
	users
INNER JOIN 
	loans
ON 
	users.user_id = loans.user_id
INNER JOIN 
	books
ON 
	loans.book_id = books.book_id

-- 5. Count of loans on each users
SELECT 
  users.user_name,
  COUNT(*) AS count_loans
FROM 
  users
INNER JOIN 
  loans
ON 
  users.user_id = loans.user_id
GROUP BY
  users.user_name

-- Books that not loans
SELECT * FROM books

-- Popular book

-- List Of loans
SELECT * FROM loans