#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
products = [
    {
        "p_id": 101,
        "p_category": "Kitchen_Appliances",
        "p_name": "2 SLICE SANDWICH MAKER Grill  (Black & Steel)",
        "brand": "Nova",
        "price": 1695,
        "image": "https://rukminim1.flixcart.com/image/416/416/k0sgl8w0/sandwich-maker/c/e/4/nova-2-slice-panni-grill-sandwich-maker-original-imafkgcmggv7me6p.jpeg?q=70"
    },
    {
        "p_id": 102,
        "p_category": "Kitchen_Appliances",
        "p_name": "Favourite IC 1800 W Induction Cooktop  (Black, Push Button)",
        "brand": "Pigeon",
        "price": 1399,
        "image": "https://rukminim1.flixcart.com/image/416/416/induction-cook-top/5/c/k/pigeon-favourite-ic-1800-w-favourite-ic-1800-w-original-imaenreqhefzd63h.jpeg?q=70"
    },
    {
        "p_id": 103,
        "p_category": "Home_Appliances",
        "p_name": "Ujala 1200 mm Energy Saving 3 Blade Ceiling Fan  (Brown, Pack of 1)",
        "brand": "Orient Electric",
        "price": 1399,
        "image": "https://rukminim1.flixcart.com/image/416/416/k0h12fk0/fan/9/z/t/ujala-ceiling-fan-1200-orient-electric-original-imafk9a2c4fghhwm.jpeg?q=70"
    },
    {
        "p_id": 104,
        "p_category": "Kitchen_Appliances",
        "p_name": "HL1655/00 250 W Hand Blender  (White)",
        "brand": "Philips",
        "price": 1550,
        "image": "https://images-na.ssl-images-amazon.com/images/I/41-5nd-r6bL._SX425_.jpg"
    },
    {
        "p_id": 105,
        "p_category": "Kitchen_Appliances",
        "p_name": "Rapid 4 Jar 750 watts 750 W Juicer Mixer Grinder  (Black, 4 Jars)",
        "brand": "Butterfly",
        "price": 2799,
        "image": "https://rukminim1.flixcart.com/image/416/416/jmi22kw0/mixer-grinder-juicer/n/z/a/butterfly-rapid-4-jar-750-watts-original-imaf5dvgugcqyug3.jpeg?q=70"
    },
    {
        "p_id": 106,
        "p_category": "Kitchen_Appliances",
        "p_name": "HR7627/00 650 W Food Processor  (White)",
        "brand": "Philips",
        "price": 4250,
        "image": "https://rukminim1.flixcart.com/image/416/416/food-processor/p/b/h/daily-collection-philips-hr7627-original-imaedkswqnfjmhu5.jpeg?q=70"
    },
    {
        "p_id": 107,
        "p_category": "Water_Purifiers",
        "p_name": "Ace Plus 8 L RO + UV + UF + TDS Water Purifier  (White)",
        "brand": "Kent",
        "price": 12999,
        "image": "https://rukminim1.flixcart.com/image/416/416/jxjahe80/water-purifier/y/g/7/kent-ace-plus-original-imafhzawerdykpeh.jpeg?q=70"
    },
    {
        "p_id": 108,
        "p_category": "Water_Purifiers",
        "p_name": "LIV-PEP-PRO-PLUS+ 7 L RO + UV + UF Water Purifier  (White)",
        "brand": "Livpure",
        "price": 9299,
        "image": "https://rukminim1.flixcart.com/image/416/416/j13vqfk0/water-purifier/8/n/7/livpure-pep-pro-original-imaesrgs2c2gtyvh.jpeg?q=70"
    },
    {
        "p_id": 109,
        "p_category": "Home_Appliances",
        "p_name": "Oeh-1220 OEH-1220 Fan Room Heater",
        "brand": "Orpat",
        "price": 1079,
        "image": "https://rukminim1.flixcart.com/image/416/416/jpsnma80/room-heater/x/d/b/oeh-1220-orpat-original-imafbyqfvmzaqrxf.jpeg?q=70"
    },
    {
        "p_id": 110,
        "p_category": "Window_Air_Conditioners",
        "p_name": "1.5 Ton 3 Star Window AC - White  (183 DZA (R32), Copper Condenser)",
        "brand": "Voltas",
        "price": 23999,
        "image": "https://rukminim1.flixcart.com/image/416/416/jy3anbk0/air-conditioner-new/z/b/y/183-dza-r32-1-5-window-fixed-speed-voltas-original-imafgbz9hpnkwhs4.jpeg?q=70"
    },
    {
        "p_id": 111,
        "p_category": "Air_Conditioners",
        "p_name": "1.5 Ton 3 Star Split Inverter AC with PM 2.5 Filter - White  (18K 3 Star Ester Neo Inverter, Copper Condenser)",
        "brand": "Carrier",
        "price": 30499,
        "image": "https://rukminim1.flixcart.com/image/416/416/jtyouq80/air-conditioner-new/s/f/8/18k-3-star-ester-neo-inverter-r32-idu-i011-18k-3star-inverter-original-imaff727rpzg3nhz.jpeg?q=70"
    },
    {
        "p_id": 112,
        "p_category": "Air_Conditioners",
        "p_name": "1.2 Ton 5 Star Split Inverter AC - White  (155V DZW (R32), Copper Condenser)",
        "brand": "Voltas",
        "price": 31499,
        "image": "https://rukminim1.flixcart.com/image/416/416/jucz98w0/air-conditioner-new/z/h/q/155v-dzw-r32-1-2-split-voltas-inverter-original-imaffdt8gyxqxfae.jpeg?q=70"
    }
]

print('''
<html>
<head>
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
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
  <a class="navbar-brand" href="#">Online Shop</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
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
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
''')

print('''
  <div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
''')

for product in products:
    print(f'''
    <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12">
    <div class="card {product["p_category"]}" style="width: 95%; height: 33rem; margin-bottom: 20px; padding: 10px">
      <img src="{product["image"]}" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">{product["brand"]} {product["p_name"]}</h5>
        <p class="card-text">Price : {product["price"]}</p>
        <a href="#" class="btn btn-primary">Add To Cart</a>
      </div>
    </div>
    </div>
  ''')

print('''
    </div>
  </div>
''')


print('''
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>
''')
