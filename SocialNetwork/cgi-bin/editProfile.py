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
                <option value="" {"selected" if data[2] == "" else ""}></option>
                <option value="student" {"selected" if data[2] == "student" else ""}>Student</option>
                <option value="employed" {"selected" if data[2] == "employed" else ""}>Employed</option>
                <option value="self-employed" {"selected" if data[2] == "self-employed" else ""}>Self Employed</option>
                <option value="engineer" {"selected" if data[2] == "engineer" else ""}>Engineer</option>
                <option value="unemployed" {"selected" if data[2] == "unemployed" else ""}>Unemployed</option>
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
            <label for="profilePic">Update Profile Picture</label><br>
            <img src="../profile_pic/{data[4]}" alt="&nbsp;No Profile Pic Found" width="100" height="100"><br><br>
            <input type="file" name="profilePic" id="profilePic" class="form-control">
        </div>
        <input type="hidden" name="email" value="{email}">
        <input type="hidden" name="oldProfilePic" value="{data[4]}">
        <button type="submit" class="btn btn-primary mb-5">Submit</button>
    </form>
    
''')

base.footer()
