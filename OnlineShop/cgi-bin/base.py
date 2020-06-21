#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import json

file = open(
    "/Users/anmolrajarora/Documents/msit-advance-python/OnlineShop/data.json")
products = json.load(file)


def getProducts():
    return products


def createProduct(product):
    print(f'''
    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
    <div class="card {product["p_category"]}" style="width: 95%; height: 33rem; margin-bottom: 20px; padding: 10px">
      <img src="{product["image"]}" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">{product["brand"]} {product["p_name"]}</h5>
        <p class="card-text">Price : {product["price"]}</p>
        <a href="cart.py?p_id={product["p_id"]}" class="btn btn-primary">Add To Cart</a>
      </div>
    </div>
    </div>
  ''')


def header():
    print('''
    <html>
    <head>
        <title>Title</title>
        <link rel="stylesheet" href="../bootstrap.min.css">
        <link rel="stylesheet" href="../design.css">
        <style>
        .card-img-top{
            align-self: center;
        }
        .card img{
            width: 210px;
        }
        </style>
    </head>
    <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-danger">
    <a class="navbar-brand" href="index.py">Online Shop</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
        <li class="nav-item active">
            <a class="nav-link" href="index.py">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item active">
            <a class="nav-link" href="#">All Products</a>
        </li>
        <li class="nav-item dropdown active">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Dropdown
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Something else here</a>
            </div>
        </li>
        <li class="nav-item active">
            <a class="nav-link" href="#">My Cart</a>
        </li>
        </ul>
        <form class="form-inline my-2 my-lg-0" action="search.py">
        <input name="q" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
        </form>
    </div>
    </nav>
    ''')


def footer():
    print('''
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    </body>
    </html>
    ''')


# products.sort(key = lambda product : product["price"])
# body{
#     background-image: url("https://st.depositphotos.com/1106005/5030/i/950/depositphotos_50304905-stock-photo-blue-small-polka-dot-pattern.jpg")
# }
