import graphviz

# Create Digraph object
dot = graphviz.Digraph()

# Define entities
entities = {
    'Library': ['Library_ID', 'Name', 'Location'],
    'Book': ['Book_ID', 'Title', 'Author', 'Year_Published'],
    'Member': ['Member_ID', 'Name', 'Address', 'Phone'],
    'Borrow': ['Borrow_ID', 'Book_ID', 'Member_ID', 'Borrow_Date', 'Return_Date']
}

# Add entities to the diagram
for entity, attributes in entities.items():
    dot.node(entity, f'{entity}\n({", ".join(attributes)})')

# Define relationships
relationships = [
    ('Library', 'Book', 'Contains'),
    ('Library', 'Member', 'Registered'),
    ('Member', 'Borrow', 'Borrows'),
    ('Book', 'Borrow', 'Borrowed_By')
]

# Add relationships to the diagram
for rel in relationships:
    dot.edge(rel[0], rel[1], label=rel[2])

# Render the diagram
dot.render('library_er_diagram', format='png', cleanup=True)
