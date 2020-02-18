username = input("Wie heißt du?")   
f = open("username.html","a")
f.write("<p>Hallo {}</p>".format(username))
f.close()   

f = open("style.css","a")
f.write("p{color:red}")
f.close()
    
f = open("username.html","a")
f.write("""<form>
      <input type="text" name="Name" placeholder="name"/>
      <input type="text" name="Email" placeholder="email"/>
      <input type="password" name="password" placeholder="password"/>
      <input type="number" name="age" placeholder="Age" value="20"/>
      
      <input type="submit" value="Absenden"/>
    </form>""")
f.close()