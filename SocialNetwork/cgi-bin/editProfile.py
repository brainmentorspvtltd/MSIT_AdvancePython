#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import cgi
import base
import model
# print("Content-type:text/html\r\n\r\n")

email = cgi.FieldStorage().getvalue("email")
base.startPage()
base.header(email)
data = model.fetchProfile(email)

print(f'''
    <h2>Edit Profile</h2>
    <hr>
    <form action="profileController.py" method="post"  enctype="multipart/form-data">
        <div class="form-group">
            <label for="contact">Contact</label>
            <input type="text" class="form-control" name="contact" id="contact" value="{data[0]}" aria-describedby="contactHelp">
            <small id="contactHelp" class="form-text text-muted">We'll never share your contact number with anyone else.</small>
        </div>
        <div class="form-group">
            <label for="dob">DOB</label>
            <input type="date" id="dob" class="form-control" name="dob" value="{data[1]}">
        </div>
        <div class="form-group">
            <label for="occupation">Occupation</label>
            <select id="occupation" class="form-control" name="occupation">
                <option value=""></option>
                <option value="student">Student</option>
                <option value="employed">Employed</option>
                <option value="self-employed">Self Employed</option>
                <option value="engineer">Engineer</option>
                <option value="unemployed">Unemployed</option>
            </select>
        </div>
        <div class="form-group">
            <label for="interest">Interest</label>
            <select id="interest" class="form-control" name="interest" >
                <option value="" {"selected" if data[3] == "" else ""}></option>
                <option value="sports" {"selected" if data[3] == "sports" else ""}>Sports</option>
                <option value="education" {"selected" if data[3] == "education" else ""}>Education</option>
                <option value="music" {"selected" if data[3] == "music" else ""}>Music</option>
                <option value="travel" {"selected" if data[3] == "travel" else ""}>Travelling</option>
                <option value="gaming" {"selected" if data[3] == "gaming" else ""}>Gaming</option>
            </select>
        </div>
        <div class="form-group">
            <label for="profilePic">Profile Picture</label>
            <input type="file" name="profilePic" id="profilePic" class="form-control" value="{data[4]}">
        </div>
        <input type="hidden" name="email" value="{email}">
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    
''')

base.footer()
