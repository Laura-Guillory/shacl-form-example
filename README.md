# shacl-form-example
This application is a minimal demonstration of how to use the
[shacl-form](https://github.com/CSIRO-enviro-informatics/shacl-form)
package. It reads the SHACL Shape stored in `shape.ttl` and uses
shacl-form to generate the files necessary to serve a form that
facilitates the input of RDF data.

`shape.ttl` contains an example SHACL Shape. You can edit this to see
how shacl-form reacts to different SHACL Shapes.


## License
This work is licensed using the GPL v3 license. See [LICENSE](LICENSE)
for the deed.

## Contacts

**Laura Guillory**  
*Lead Developer*  
Informatics Software Engineer at CSIRO Land & Water  
<laura.guillory@csiro.au>

**Nicholas Car**  
*Product Owner*  
Senior Experimental Scientist  
CSIRO Land & Water  
<nicholas.car@csiro.au>

## How to use

* Run app.py
* Navigate to http://localhost:5000/
* Click 'Generate Form'. The application will read `shape.ttl` and
generate all the files necessary to serve the form
* Fill out the form and submit
* The results will be stored in `result.ttl`

shacl-form generates two files:
* `view/templates/form_contents.html` is a Jinja2 template which extends
`form.html`. You will want to edit `form.html` to control where your
form appears on your site.
* `map.ttl` is a Turtle RDF file which is used to convert information
submitted to the form back into RDF.

These two files are a pair and can't be interchanged with files
generated for another shape. They will only need to be generated once,
but if you want to change the form, you can delete them to generate new
ones.