book = {
    "Title " : "Atomic Habits",
    "Author " : "James Clear",
    "ISBN " : "234-23-2-523",
    "Page_Count ": 250
}

# Accessing Values
print(book["Title "])
book["Title "] = "2020 What weng wrong"
print(book["Title "])
print(book)

# Keys
keys = book.keys()
print(keys)

# List of Dictionaries

personalities = [
    {
       "Name":"Tuqeer",
       "Age" : 19
},{
       "Name":"Tanveer",
       "Age" : 23
}               
]
print(personalities)

# A bag dictionary

bag = {
    "books" : [{
    "Title " : "Atomic Habits",
    "Author " : "James Clear",
    "ISBN " : "234-23-2-523",
    "Page_Count ": 250
    },{
    "Title " : "Nuclear Habits",
    "Author " : "James Dull",
    "ISBN " : "234-23-2-623",
    "Page_Count ": 350
    }],
    "Stationary":[
        {
            "Name": "Pencil",
            "Quantity" : 2
        },{
            "Name": "Ball Pen",
            "Quantity": 2
        }
    ],
    "Size":"14",
    "Color":"Black"   
}
print(bag)
