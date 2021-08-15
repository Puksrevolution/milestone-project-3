Milestone Project 3
======

## **Testing Details** ##

[Main README.md file](https://github.com/Puksrevolution/milestone-project-3)

[View the live project here.](http://msp3-cookbook.herokuapp.com/)

---

    
# Table of contents

- [Automated Testing](#automated-testing)
  - [Validation Services](#validation-services)
- [Manual Testing](#manual-testing)
  - [Unit Testing](#unit-testing)
  - [Testing the responsivity of different screen sizes](#testing-the-responsivity-of-different-screen-sizes)
  - [Browser testing undertaken on Laptop](#browser-testing-undertaken-on-laptop)
  - [Testing undertaken on smartphone device](#testing-undertaken-on-smartphone-device)  

---

Automated Testing
======

## **Validation Services** ##

The following **validation services** and **linters** were used to check the validity of the website code.


- [W3C Markup Validation](https://validator.w3.org/) 
  - This validator checks the markup validity of Web documents in HTML, XHTML, SMIL, MathML, etc.

  ![Result](/Documentation/test/html-index-validator.png)
  ![Result](/Documentation/test/html-all_recipe-validator.png)
  ![Result](/Documentation/test/html-view_recipe-validator.png)  
  ![Result](/Documentation/test/html-signup-validator.png)
  ![Result](/Documentation/test/html-signin-validator.png)
  ![Result](/Documentation/test/html-add_recipe-validator.png)

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
  - This validator checks the validity of cascading style sheets (css) and (X)HTML documents with style sheets.

  ![Result](/Documentation/test/css-validatior.png)
Two Error messages for Bootstrap CSS <br>
Dev: CSS code is Valid
  

- [PEP8 Online validation](http://pep8online.com)
  - This linter checks the validity of Python code against the PEP8 requirements
    ![PEP8 results image](/Documentation/test/pep8-online.png)

- [Chrome DevTools Lighthouse](https://developers.google.com/web/tools/lighthouse)
  - An open-source automated tool for improving webpages by running audits for performance, accessibility, progressive web apps, SEO etc.


  - ### **Desktop Performance Report** ###

    ![Google Lighthouse - Desktop](/Documentation/test/lighthouse-desktop.png)    
  

  - ### **Mobile Performance Report** ###

    ![Google Lighthouse - Mobile](/Documentation/test/lighthouse-mobile.png)

Manual Testing
======

### **Unit Testing** ###
[Unit Testing document](test/unit-testing.pdf) containing:
- The test cases
  - Test Cases  
  - Expected Output
  - Pass/Fail

### **Testing the responsivity of different screen sizes** ###

- Hardware:
    - ThinkPad E14 Gen Laptop 
    - 14,0" FHD (1920 × 1080) TN antireflex, 220 cd/m²    
- Tested Operating Systems:
   - Windows 10 Pro 64
- Tool:
    - [What is my Screen Resolution](http://whatismyscreenresolution.net/)
      - An online tool to find out the screen resolution on your device used for CSS @media queries   
   
| Device | Screen size | Pass/Fail |
| :---: | --- | :---: |
| Desktop | all | Pass |
| Mobile | all | one Fail |
| LG Optimus One | 213 x 320 | Fail |
| Tablet | all | Pass |
| Television | all | Pass |


### **Browser testing on Laptop** ###
- Hardware:
    - ThinkPad E14 Gen Laptop 
    - 14,0" FHD (1920 × 1080) TN antireflex, 220 cd/m²    
- Tested Operating Systems:
    - Windows 10 Pro 64

​
| Browser | Version | Pass/Fail |
| :---: | --- | :---: |
| Chrome | 90.0.4430.212 | Pass |
| Firefox | 87.0 | Pass |
| Edge | 90.0.818.56 | Pass |
| Opera | 76.0.4017.107 | Pass |

### **Testing undertaken on smartphone device** ###

- Hardware:
    - Galaxy A20e 5.80"
- Tested Operating Systems:    
    - Android 10

| Browser | Version | Pass/Fail |
| :---: | --- | :---: |
| Samsung |13.2.1.70 | Pass |
| Chrome | 81.0.4044.138 | Pass |
| Firefox | 88.1.3 | Pass |
