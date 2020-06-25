#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import base

base.header()

print('''
    <h2>Edit Profile</h2>
    <hr>
    <form action="profileController.py" method="post"  enctype="multipart/form-data">
        <div class="form-group">
            <label for="contact">Contact</label>
            <input type="text" class="form-control" name="contact" id="contact" aria-describedby="contactHelp">
            <small id="contactHelp" class="form-text text-muted">We'll never share your contact number with anyone else.</small>
        </div>
        <div class="form-group">
            <label for="dob">DOB</label>
            <input type="date" id="dob" class="form-control" name="dob">
        </div>
        <div class="form-group">
            <label for="occupation">Occupation</label>
            <select id="occupation" class="form-control" name="occupation">
                <option value="student">Student</option>
                <option value="employed">Employed</option>
                <option value="self-employed">Self Employed</option>
                <option value="engineer">Engineer</option>
                <option value="unemployed">Unemployed</option>
            </select>
        </div>
        <div class="form-group">
            <label for="interest">Interest</label>
            <select id="interest" class="form-control" name="interest">
                <option value="sports">Sports</option>
                <option value="education">Education</option>
                <option value="music">Music</option>
                <option value="travel">Travelling</option>
                <option value="gaming">Gaming</option>
            </select>
        </div>
        <div class="form-group">
            <label for="profilePic">Profile Picture</label>
            <input type="file" name="profilePic" id="profilePic" class="form-control">
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
''')

base.footer()
