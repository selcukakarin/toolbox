Kendime notlar
#######
{# Include the hidden fields #}
{% for hidden in form.hidden_fields %}
    {{ hidden }}
{% endfor %}

{# Include the visible fields #}
{% for field in form.visible_fields %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
    </div>
{% endfor %}
This may also be useful: {{ form.field.as_hidden }}
#######
form.fields['field_name'].widget = forms.HiddenInput()
#######
forms.CharField(widget = forms.HiddenInput(), required = False)
#######
>>> f = ContactForm()
>>> print(f)
<tr><th><label for="id_subject">Subject:</label></th><td><input id="id_subject" type="text" name="subject" maxlength="100" required></td></tr>
<tr><th><label for="id_message">Message:</label></th><td><input type="text" name="message" id="id_message" required></td></tr>
<tr><th><label for="id_sender">Sender:</label></th><td><input type="email" name="sender" id="id_sender" required></td></tr>
<tr><th><label for="id_cc_myself">Cc myself:</label></th><td><input type="checkbox" name="cc_myself" id="id_cc_myself"></td></tr>
#######
self.fields['acknowledge'].required = False
#######
from django import forms

class ContactForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'

    # ... and the rest of your fields here
#######
<input type="email" pattern="/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@gmail.com$" />
#######
{{cari_formu.hesapKodu.errors}}
#######
for visible in self.visible_fields():
            self.fields[visible.name].error_messages = {
                'invalid': 'Girilen değer uygun bir sayı değeri değildir. ----',
                'required': 'Bu alan boş geçilemez ----'
                }
#######
class NewsletterForm(forms.ModelForm):

    email = forms.EmailField(
      widget=forms.EmailInput(attrs={
        'autocomplete': 'off',
        'class': 'form-control',
        'placeholder': _('seuemail@email.com'),
        'required': 'required'
      }),
      error_messages={'invalid': 'your custom error message'}
    )

    class Meta:
        model = Newsletter
        fields = ['email', ]
######
 from django.core.validators import EmailValidator

   email = models.EmailField(validators=[EmailValidator(message="your custom message")]) # in you model class
######
exclude = ['hesapKodu']
######
#setattr
@login_required(login_url="Kullanici:kullanici_giris")
def editableTableChange_sysRefTip(request,id):

	# aliasLng1 - değişen kolon
	col_nm=request.POST.get("editColName")
	# AdresUlkeKod12 - değişen cell'in son değeri
	chg_val=request.POST.get("editColVal")
	# değişen obje
	obj = SysRefTip.objects.get(id=id)
	# değişen objenin değişen kolonunu son değerle güncelle
	setattr(obj , col_nm, chg_val)
	obj.save()
	#MyModel.objects.filter(pk=some_value).update(field1='some value')

	#messages.info(request, "\'" + cari_verisi.unvan + "\'" + "{}".format(_(": Koduna Sahip Değer Güncellendi")))
	return redirect("Table_definition:table")
######
obj, created = Person.objects.get_or_create(first_name='John', last_name='Lennon',
                  defaults={'birthday': date(1940, 10, 9)})
[Kaynak](https://kite.com/python/docs/django.db.models.query.QuerySet.get_or_create)
######
var airlineSelected = $('#airline-selected').find(":selected").val();
######
[Kaynak](https://stackoverflow.com/questions/53442223/django-search-multiple-fields-of-a-django-model-with-multiple-input-field-with)
url(r'^search_cars/$'. views.search_cars, name='search-cars')

def search_cars(request, *args, **kwargs):
    content_type = 'application/json'

    # I think you only need ajax, but you can choose to remove this
    if request.is_ajax():
        brand = request.GET.get('brand')
        colour = request.GET.get('colour')
        year = request.GET.get('year')

        # checking if all 3 are present
        if brand is None or color is None or year is None:
            return HttpResponse({
                'success': False,
                'message': 'Required fields are missing.'
            }, content_type=content_type)

        # depending on how you want to filter
        # this will choose cars which have either brand, colour or year
        filters = Q(Q(brand=brand) | Q(color=colour) | Q(year=year))
        second_hand_cars = SecondHandCars.objects.filter(filters)

        # or
        # you can choose cars which satisfy all three of these together
        filters = {'brand': brand, 'colour': colour, 'year': year}
        second_hand_cars = SecondHandCars.objects.filter(**filters)

        # serialize the objects and return the json response
        data = []
        for car in second_hand_cars:
            data.append({
                'brand': car.brand,
                'colour': car.colour,
                'year': car.year,
                'description': car.description,
                'slug': car.slug
            })

        return HttpResponse({
            'success': True,
            'data': data,
        }, content_type=content_type)
    else:
        return HttpResponse({
            'success': False,
            'message': 'Only AJAX method is allowed.'
        }, content_type=content_type)

// JavaScript code to make an ajax request
// when all three dropdowns are selected with appropriate values.
// assuming you are using jQuery.

// add a common class to all 3 dropdowns to monitor changes
$(document).on('change', '.filter-dropdown', function() {
    # all three will provide attribute `value` of `option` tag.
    var brand = $('#brandDropdown').children('option:selected').val();
    var colour = $('#colourDropdown').children('option:selected').val();
    var year = $('#yearDropdown').children('option:selected').val();

    # add a default selected `option` tag with value `""`
    if (brand !== "" && colour !== "" && year !== "") {
        var data = {
            'brand': brand,
            'colour': colour,
            'year': year
        }

        $.ajax({
            url: '/search_cars/',
            type: 'GET',
            data: data,
            dataType: 'json',
            success: function(response) {
                if (response.success) {
                    // render cars from `response.data`
                } else {
                    // show message from `response.message`
                }
            },
            error: function(errorResponse) {
                // show error message
            }
        });
    } else {
        return;
    }
});
######
equipo = ChoiceField(
        widget=Select(
            attrs={'class': 'form-control input-sm', 'multiple': 'multiple'}
        )
    )
######
<script>
    var array_equipos = {{ equipos_lista }};
    $('#id_equipo').val(array_equipos);
    $('#id_equipo').trigger('change');

 </script>
######
        <input list="brow">
        <datalist id="brow">
          <option value="Internet Explorer">
          <option value="Firefox">
          <option value="Chrome">
          <option value="Opera">
          <option value="Safari">
        </datalist>  
######
https://stackoverflow.com/questions/49172762/how-to-access-the-value-from-select2-in-django
######
Create an Article via the Reporter object:

>>> new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
>>> new_article
<Article: John's second story>
>>> new_article.reporter
<Reporter: John Smith>
>>> new_article.reporter.id
[Kaynak](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_one/)
######
from django import forms
from django.contrib import admin 
from models import *

class SupplierAdminForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__" # for Django 1.8+


    def __init__(self, *args, **kwargs):
        super(SupplierAdminForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['cat'].queryset = Cat.objects.filter(supplier=self.instance)
[Kaynak](https://stackoverflow.com/questions/232435/how-do-i-restrict-foreign-keys-choices-to-related-objects-only-in-django)
######
[Kaynak](https://stackoverflow.com/questions/16669422/django-join-query-without-foreign-key)
[Kaynak](https://stackoverflow.com/questions/12681992/most-efficient-way-to-use-the-django-orm-when-comparing-elements-from-two-lists)
First problem: joining unrelated models
I'm assuming that your Model1 and Model2 are not related, otherwise you'd be able to use Django's related objects interface. Here are two approaches you could take:

Use extra and a SQL subquery:

Model1.objects.extra(where = ['field in (SELECT field from myapp_model2 WHERE ...)'])
Subqueries are not handled very efficiently in some databases (notably MySQL) so this is probably not as good as #2 below.

Use a raw SQL query:

Model1.objects.raw('''SELECT * from myapp_model1
                   INNER JOIN myapp_model2
                   ON myapp_model1.field = myapp_model2.field
                   AND ...''')
Second problem: enumerating the result
Two approaches:

You can enumerate a query set in Python using the built-in enumerate function:

enumerate(Model1.objects.all())
You can use the technique described in this answer to do the enumeration in MySQL. Something like this:

Model1.objects.raw('''SELECT *, @row := @row + 1 AS row
                   FROM myapp_model1
                   JOIN (SELECT @row := 0) rowtable
                   INNER JOIN myapp_model2
                   ON myapp_model1.field = myapp_model2.field
                   AND ...''')
######
[Kaynak](https://stackoverflow.com/questions/5708650/how-do-i-add-a-foreign-key-field-to-a-modelform-in-django)
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['user_defined_code']=forms.ModelChoiceField(queryset=UserDefinedCode.objects.filter(owner=user))
######
bolgeKod = forms.ModelChoiceField(queryset=SysReferans.objects.none())
self.fields['bolgeKod'].queryset = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='bolgeKod').values("reftype_id")[0]["reftype_id"]))
Seçenek True kontrolü = SysRefTip.objects.filter(Q(id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"])).values("Secenekler")[0]['Secenekler'] == True)
ref_type_id değeri var mı kontrolü ( Yani sysColumns'da atama yapılmış mı kontrolü ) = sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]
if (sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"] != None and SysRefTip.objects.filter(Q(id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"])).values("Secenekler")[0]['Secenekler'] == True):
    self.fields['{}'.format(visible.name)].queryset = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]))
else:
    self.fields['{}'.format(visible.name)].queryset = SysReferans.objects.none()
######
return u'<option value="%s"%s%s>%s</option>' % (
            escape(option_value), title_html, selected_html,
            conditional_escape(force_unicode(option_label)))""
######
#.exclude(Q(id=None)|Q(Tip=None)|Q(Kod=None)|Q(Aciklama1=None)|Q(Aciklama2=None)|Q(GrupKod=None)|Q(SayKod=None))
######
    if (sysColumns.objects.filter(name='{}'.format('bolgeKod')).values("reftype_id")[0]["reftype_id"] != None and SysRefTip.objects.filter(Q(id=sysColumns.objects.filter(name='{}'.format('bolgeKod')).values("reftype_id")[0]["reftype_id"])).values("Secenekler")[0]['Secenekler'] == True):
        # self.fields['{}'.format(visible.name)].queryset = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]))
        titles = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='{}'.format('bolgeKod')).values("reftype_id")[0]["reftype_id"]))
        cari_formu.fields['bolgeKod'].choices = [('C1', 'Choice1'), ('C2', 'Choice2')]
    else:
        cari_formu.fields['{}'.format('bolgeKod')].choices = None
######
for visible in self.visible_fields():
try:
    # Seçenekler True kontrolü = SysRefTip.objects.filter(Q(id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"])).values("Secenekler")[0]['Secenekler'] == True)
    # ref_type_id değeri var mı kontrolü ( Yani sysColumns'da atama yapılmış mı kontrolü ) = sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]
    if (sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"] != None and SysRefTip.objects.filter(Q(id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"])).values("Secenekler")[0]['Secenekler'] == True):
        # self.fields['{}'.format(visible.name)].queryset = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]))
        titles = SysReferans.objects.filter(Q(Tip_id=sysColumns.objects.filter(name='{}'.format(visible.name)).values("reftype_id")[0]["reftype_id"]))
        self.fields['{}'.format(visible.name)].choices = [(title.Kod, title.Kod) for title in titles]
    else:
        self.fields['{}'.format(visible.name)].choices = None

except:
    pass
######
selectize init option ekleme
[kaynak](https://stackoverflow.com/questions/21962124/how-to-set-a-value-for-a-selectize-js-input)
$('.kod').selectize({
      valueField: 'Kod',
      labelField: 'Kod',
      searchField: 'Kod',
      placeholder: 'Seçim yapınız...',
      create: false,
      options: [  ],
      onChange: function(val) {
        fieldName=this["$input"][0]
        // onChange ile kod alanlarında bir değişiklik var ise gerekli required atamaları yapılır.
        if(val != ''){
          // eğer değişiklikten sonra bir seçim var ise selectize inputuna required özelliği atanır
          // ve aynı zamanda flag class'ı eklenir. flag class'ı bu if blogunun kontrollerinde kullanılan required özelliği yerine kullanılacaktır.
          if(fieldName.nextSibling.firstChild.firstChild.nextSibling){
            x=fieldName.nextSibling.firstChild.firstChild.nextSibling.required = false;
            fieldName.nextSibling.firstChild.firstChild.nextSibling.classList.add("flag");
          }
        }
        else{
          if(fieldName.nextSibling.firstChild.firstChild.className == "flag"){
            x=fieldName.nextSibling.firstChild.firstChild.required = true;
          }
        }
      },
      onInitialize:  function () {
        var selectize = this;
        console.log("selam")
        fieldName=this["$input"][0]["name"]
        console.log("00000")
        console.log(fieldName)
        $.get(`{% url 'Cari:fillToSelectizeInit' %}?searchKey=${fieldName}`, function( data ) {
            selectize.addOption(data); // This is will add to option
            /*var selected_items = [];
            $.each(data, function( i, obj) {
                selected_items.push(obj.id);
            });
            selectize.setValue(selected_items); //this will set option values as default*/
        });
      },
      load: function (query, callback) {
        if (!query.length) return callback();
        $.ajax({
          url: "{% url 'Cari:fillToSelectize' %}", //'http://127.0.0.1:8888/en-gb/Referans/test/kolon',
          async: false,
          type: 'GET',
          dataType: 'json',
          data: {
            searchVal: query,
            searchKey:searchKey,
          },
          error: function () {
            callback();
          },
          success: function (res) {
            callback(res)
          }
        })
      }
    });
######
[kaynak](https://stackoverflow.com/questions/47893324/django-form-choicefield-set-choices-in-view-in-form-initial)
form = Form()
form.fields['title'].choices = [(title.title, title.title) for title in titles]
form.fields['title'].initial = titles[0].title  # by default first will be selected
######
How to change empty_label for modelForm choice field?
[Kaynak](https://stackoverflow.com/questions/12984013/how-to-change-empty-label-for-modelform-choice-field)
[Kaynak](https://stackoverflow.com/questions/8928565/django-cant-remove-empty-label-from-typedchoicefield)
######
Form ChoiceField alana option ekleme
class PayrollCredentialForm(forms.ModelForm):
    class Meta:
        model = Company
    def __init__(self, *args, **kwargs):
        super(PayrollCredentialForm, self).__init__(*args, **kwargs)
        self.fields["payrollProvider"].choices = [("", "please choose value"),] + list(self.fields["payrollProvider"].choices)[1:] 
[Kaynak](https://stackoverflow.com/questions/12984013/how-to-change-empty-label-for-modelform-choice-field)
######
Selectize: Setting Default Value in onInitialize with setValue
[Kaynak](https://stackoverflow.com/questions/37819934/selectize-setting-default-value-in-oninitialize-with-setvalue)
######
ModelChoiceField initial value 
form = SupplyTypeForm(request.POST or None, 
                      initial={'service_type': User.DUAL_SUPPLIER})
Or do it in the constructor of the form:

class SupplyTypeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SupplyTypeForm, self).__init__(*args, **kwargs)
        self.fields['sevice_type'].initial = User.DUAL_SUPPLIER
[Kaynak](https://stackoverflow.com/questions/34996613/django-model-form-initial-value-on-choicefield)
######
self.fields['mcq_answer_choice'].queryset = queryset
class QuizUserForm(forms.Form):
    question = forms.CharField()
    eq_answer = forms.CharField(widget=forms.Textarea)
    mcq_answer_choice = forms.ModelChoiceField(
        queryset=models.MCQChoice.objects.none(),
        widget=forms.RadioSelect,
        empty_label=None
    )

    def __init__(self, *args, **kwargs):
        super(QuizUserForm, self).__init__(*args, **kwargs)
        queryset = models.MCQChoice.objects.filter(
            question__prompt=kwargs['initial']['question']
        )
        self.fields['mcq_answer_choice'].queryset = queryset
        self.fields['mcq_answer_choice'].initial = queryset.first()
[Kaynak](https://stackoverflow.com/questions/40882840/specify-initial-choice-for-a-form-modelchoicefield)
######
QuerySet'leri liste çevirip json response olarak gönderme
    list_data_json = list(searchQuery)
    chosenVal = list(Cari.objects.filter(id=uuid).values(searchKey))
    return JsonResponse({'list_data_json': list_data_json,'chosenVal':chosenVal})
[Kaynak](https://stackoverflow.com/questions/16790375/django-object-is-not-json-serializable)

######
    @classmethod
    def getAllTblColumnsName(cls):
        table_names=cls.getAllTableNames()
        cursor=connection.cursor()
        columns_ınfo={}
        
        for tbl in table_names:
            cursor.execute('''  SELECT column_name
                            FROM information_schema.columns
                            WHERE table_schema = 'public'
                            AND table_name   = '%s'; ''' % str(tbl) )
            count=0
            columns_list=[]
            print("TEST CURSOR COLUMNS")
            for c in cursor:
                print(c[count])
                columns_list.append(c[count])
            columns_ınfo[tbl]=columns_list   
       
            
        print(columns_list)
        print(columns_ınfo)
        return columns_ınfo 
######
 @classmethod
    def getAllTableNames(cls):

        cursor=connection.cursor()
        cursor.execute(''' SELECT table_name
                         FROM information_schema.tables
                         WHERE table_schema='public'
                         AND table_type='BASE TABLE'
                         AND table_name not Like  'django%'
                         AND table_name not Like  '%auth%'
                         
                         AND table_name not Like  '%user_per%'
                         AND table_name not Like  '%group%'
                         AND table_name not in('TblGorselAyarlar','sysTables','sysColumns','sysHistory','sysComboItems','sysCombo','sysVersionInfo','sysSifrePolitikalari'); ''' )
        count=0
        table_names=[]
        print("TEST CURSOR")
        for c in cursor:
            print(c[count])
            table_names.append(c[count])
        print(table_names)
        return table_names
######
def getColumnsLength(request):

     cursor=connection.cursor()
     cursor.execute(''' SELECT column_name,character_maximum_length
                              FROM INFORMATION_SCHEMA.COLUMNS
                              WHERE table_schema='public'
                         AND table_name not Like  'django%'
                         AND table_name not Like  '%auth%'
                         AND table_name not Like  '%User%'
                         AND table_name not Like  '%user_per%'
                         AND table_name not Like  '%group%'
                         AND table_name not in('TblGorselAyarlar','sysTables','sysColumns','sysHistory','sysComboItems','sysCombo','sysVersionInfo','sysSifrePolitikalari'); ''' )

     dict1={}
     for c in cursor:
       
          dict1[c[0]]=c[1]
     return dict1
######
table_id=sysTables.objects.values('id').get(name=str(t))
registered_columns=sysColumns.objects.filter(table_id=table_id["id"]).values("name")
######
context = {
            "id":id,
            "tblNameStr":tblNameStr,
            "uygulama_adi":uygulama_adi,
            "url_adi":url_adi,
            "getcsvpdf":request.GET.get("getcsvpdf","Sayfalı"),
        }
        
        context.update(kolon_context)  
######
Overriding choicefield
[Kaynak](https://stackoverflow.com/questions/53190973/django-forms-choicefield-overriding-forms-init)
######
Forma initial value ekleme
[Kaynak](https://stackoverflow.com/questions/34190091/how-override-init-add-instance-forms-form-django)
[Kaynak2](https://stackoverflow.com/questions/2599893/django-form-creation-on-init)
######
form init from view
[Kaynak](https://stackoverflow.com/questions/28204421/how-can-i-pass-a-value-to-django-forms-init-method-from-a-view)
######
Add class to form field Django ModelForm
[Kaynak](https://stackoverflow.com/questions/29716023/add-class-to-form-field-django-modelform)
class ExampleForm(forms.Form):
    # Your declared form fields here
    ...

    def __init__(self, *args, **kwargs):
        super(ExampleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
######
class NewsForm(ModelForm):
    class Meta:
        model = News_Article
        exclude = ('news_datetime_submitted', 'news_yearmonth', )
        labels = {
            'news_title': _('Enter News Title'),
        }
        help_texts = {
            'news_title': _('Enter a title to give a short description of what the news is.'),
        }
        error_messages = {
            'news_title': {
                'max_length': _("News title is too long."),
            },
        }
######
[Kaynak](https://stackoverflow.com/questions/45760218/invalid-literal-for-int-with-base-10-django-python)
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    news_title = models.CharField(max_length=420, help_text="Insert only the news title, be specific and short!")
    pub_date = models.DateTimeField('date published')
    article_text = RichTextField()
    news_author = models.CharField(User, max_length=250, editable = False, default='unknown')

    class Meta:
        ordering = ["news_title", "-pub_date"]
        verbose_name = "News"
        verbose_name_plural = "News"

    def get_absolute_url(self):
        return reverse('model-detail-view', args[str(self.id)])

    def __str__(self):
        return self.news_title
######
        ######## visible
        # for visible in self.visible_fields():
        #     self.fields[visible.name].error_messages = {
        #         'invalid': 'Bu alan için uygun bir değer giriniz. ----',
        #         'required': 'Bu alan boş geçilemez ----'
        #         }
            # if visible.name == 'kdvTevfikatUygula' or visible.name == 'kdvMuaf' or visible.name == 'formBaBsUnvan':
                visible.label_classls
                es = ('form-label-custom-chk',)
        #     elif visible.name != 'bolgeKod' and visible.name != 'ozelKod' and \
        #     visible.name != 'grupKod' and visible.name != 'tipKod' and \
        #     visible.name != 'mhsKod' and visible.name != 'masrafMerkezi' :
        #         visible.field.widget.attrs['class'] = 'form-input-custom form-control'
        #         visible.label_classes = ('form-label-custom',)
        #     for key,val in AllColumns.items():
        #         # perDataCache metodu ile gelen kolon değerlerinin ilk harfi büyük geldiği için aşağıdaki komutu kullandık
        #         key=key.lower()
        #         key = key[0].upper() + key[1:]
        #         # x=visible.label
        #         if visible.label == key:
        #             visible.label = val
        ######## visible
######
dvzTL = forms.ModelChoiceField(
            required=False,
            queryset=sysComboItems.objects.filter(
                                        Q(combo_id=sysColumns.objects.filter(name='dvzTL').values("combo_id")[0]["combo_id"])),
            empty_label="----------------",
            label="dvzTL",
            widget=forms.Select(attrs={
                'placeholder': '','id':'dvzTL','class':''
              }))
######
def get_location_choices():
        cursor = connection.cursor()
        # cursor.execute('''SELECT co.nameLng1 FROM public."sysCombo" comb INNER JOIN public."sysComboItems" co ON (comb.id = co.comboid_id) WHERE comb.name = 'Doviz/TL' ''')    
        return cursor.fetchall()
######
dovizIslemKurCins = forms.ChoiceField(choices=(0, ('','---------' )),required=False)
######
class CariFormu(forms.ModelForm):
    class Meta:
        model = Cari
        fields = '__all__'
        
        dovizIslemKurCins = forms.ChoiceField(choices=(0, ('','---------' )),required=False)
        
        widgets = {
                'hesapKodu':forms.TextInput(attrs={'placeholder': ''}),
                'unvan': forms.TextInput(attrs={'placeholder': ''}),
                'ad': forms.TextInput(attrs={'placeholder': ''}),
                'soyad': forms.TextInput(attrs={'placeholder': ''}),
                'dovizCinsi':  forms.TextInput(attrs={'placeholder': '',}),
                'krediLimiti': forms.NumberInput(attrs={'placeholder': '','data-mask':"999 ₺"}),
                'dvzKrediLimiti': forms.NumberInput(attrs={'placeholder': '','data-mask':"999 ₺"}),
                'bolgeKod': forms.Select(attrs={'placeholder': '','id':'bolgeKod','class':'kod','style':'width:100%'}),
                'ozelKod': forms.Select(attrs={'placeholder': '','id':'ozelKod','class':'kod','style':'width:100%'}),
                'grupKod': forms.Select(attrs={'placeholder': '','id':'grupKod','class':'kod','style':'width:100%'}),
                'tipKod': forms.Select(attrs={'min':'0','placeholder': '','id':'tipKod','class':'kod','style':'width:100%'}),
                'mhsKod': forms.Select(attrs={'placeholder': '','id':'mhsKod','class':'kod','style':'width:100%'}),
                'masrafMerkezi': forms.Select(attrs={'placeholder': '','id':'masrafMerkezi','class':'kod','style':'width:100%'}),
                'resim': forms.FileInput(attrs={'id':'files','style':'margin:auto;width: 116px !important; height: 42px !important;'}),
                'vergiDairesi': forms.TextInput(attrs={'placeholder': '','data-mask':"999999"}),
                'hesapNo': forms.TextInput(attrs={'placeholder': ''}),
                'faturaChk': forms.TextInput(attrs={'placeholder': ''}),
                'iskontoOran': forms.NumberInput(attrs={'placeholder': '','data-mask':"99%"}),
                'opsiyonGunu': forms.NumberInput(attrs={'min':'0','placeholder': '','id':'opsiyonGunu',}),
                'chKodu': forms.TextInput(attrs={'placeholder': ''}),
                'kdvTevfikatUygula': forms.CheckboxInput(attrs={'placeholder': '','style':'margin:4px 0 0 0;','id':'kdvTevfikatUygula',
                'class':'form-input-styled'}),
                'kdvMuaf': forms.CheckboxInput(attrs={'placeholder': '','style':'margin:4px 0 0 0;','id':'kdvMuaf',
                'class':'form-input-styled'}),
                'kdvMuafAck': forms.TextInput(attrs={'placeholder': '','class':'form-control form-input-custom'}),
                'formBaBsUnvan': forms.CheckboxInput(attrs={'placeholder': '','style':'margin:4px 0 0 0;','id':'formBaBsUnvan','class':'form-input-styled'}),
                'sirketEMail': forms.TextInput(attrs={'placeholder': ''}),
                'sirketWebAdres': forms.TextInput(attrs={'placeholder': ''}),
                'satIslemEMail': forms.TextInput(attrs={'placeholder': ''}),
                'satAlmaIslemEMail': forms.TextInput(attrs={'placeholder': ''}),
                'finIslemEMail': forms.TextInput(attrs={'placeholder': '','class':'form-control form-input-custom'}),
                'odemePlani': forms.TextInput(attrs={'placeholder': '','id':'odemePlani'}),
            }
######
for visible in self.visible_fields():
            for key,val in AllColumns.items():
                # perDataCache metodu ile gelen kolon değerlerinin ilk harfi büyük geldiği için aşağıdaki komutu kullandık
                key=key.lower()
                key = key[0].upper() + key[1:]
                if visible.label==key:
                    visible.label = val
        columns = sysColumns.objects.values_list("name","visible").filter(table_id=sysTables.objects.values_list("id").get(name='CariErisim'))
######
for visible in self.visible_fields():
            for key,val in AllColumns.items():
                # perDataCache metodu ile gelen kolon değerlerinin ilk harfi büyük geldiği için aşağıdaki komutu kullandık
                key=key.lower()
                key = key[0].upper() + key[1:]
                if visible.label==key:
                    visible.label = val
######
class CariEBilgiFormu(forms.ModelForm):

    EFatSenaryo = forms.ChoiceField(choices=ProfileID, required=False, label=_('Pseudo'), widget=forms.Select(attrs={
        'placeholder': '','class':'form-control form-input-custom'
        })),
    EIrsSenaryo = forms.ChoiceField(choices=ProfileID, required=False, label='SELCUK', widget=forms.Select(attrs={
            'placeholder': '','class':'form-control form-input-custom '
            })),  
   
    
    class Meta:
        model = CariEBilgi

        EFatSenaryo = forms.ChoiceField(choices=ProfileID,required=False)
        EIrsSenaryo = forms.ChoiceField(choices=ProfileID,required=False)
######
class KullaniciOlusturmaFormu(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username","password","first_name","last_name","email","is_superuser","is_staff", "is_active","resim"]

        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password':forms.PasswordInput(attrs={'class':'form-control form-control-user','autocomplete':'new-password'}),
            'first_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'last_name':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'email':forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'is_superuser': forms.CheckboxInput(attrs={'class':'custom-control-input','id':'super'}),
            'is_staff':forms.CheckboxInput(attrs={'class':'custom-control-input','id':'staff'}),
            'is_active':forms.CheckboxInput(attrs={'class':'custom-control-input','id':'active','checked':''}),
            'resim':forms.FileInput(attrs={'id':'files'}),
        }

        labels = {
            'username':_('Kullanıcı Adı'),
            'password':_('Şifre'),
            'first_name':_('İsim'),
            'last_name':_('Soyisim'),
            'email':_('Email'),
            'is_superuser':_('Süper Kullanıcı'),
            'is_staff':_('Personel'),
            'is_active':_('Aktif'),
        }
######
error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Veritabanında Kod ve Tip_id değerlerinin aynı olduğu başka bir kayıt mevcuttur. Lütfen farklı bir kayıt giriniz.",
            }
        }
######
Django choicefielda viewda seçilebilir option ekleme
"""in forms"""
class ColumnsDefinitionsForms(forms.ModelForm):
    
    datatype = forms.ChoiceField(choices=DataTypes, required=False, label='Alan Veri Tipi' ,
    widget=forms.Select(attrs={'placeholder': '','class':'form-control select-access-open select2-hidden-accessible popUp'}))
    
    name = forms.ChoiceField()
"""in view"""
colDefForm.fields['name'].choices = [(title,title) for title in columnValues]
[Kaynak](https://stackoverflow.com/questions/47893324/django-form-choicefield-set-choices-in-view-in-form-initial)
form = Form()
form.fields['title'].choices = [(title.title, title.title) for title in titles]
form.fields['title'].initial = titles[0].title  # by default first will be selected
######
<div class="form-input_group">
    {% for field in cariEBilgi_formu %}
    <div class="flex-cell">
        <label for="" class="{% for class in field.label_classes %}{{ class }} {% endfor %}">{{field.label}}
        </label>
        {{field}}
    </div>

    {% endfor %}
</div>
######
db'ye oto kayıt girme
aa = ['A','B','C','D','F','L','U','G','N','M','O']
    bb = ['1','2','3','4','5','6','7','8','9','0']

    cumle1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque id justo non tellus posuere fermentum tincidunt ut sapien. Nullam diam nisl, dignissim ac convallis eget, dapibus a odio. In quis elementum dui. Duis sed lacus vel odio porta tempus. Ut erat risus, dignissim quis tincidunt eu, suscipit vitae quam. Cras arcu neque, tempus bibendum metus ut, ultrices sodales magna. Sed consectetur maximus massa at maximus. Donec nec semper sem, rhoncus elementum mauris. Curabitur ornare in nisl sit amet pellentesque. Pellentesque at lectus vel nunc mollis dapibus "
    cumle2 = "Phasellus viverra dui at convallis accumsan. Sed eu sodales metus. Nunc imperdiet tortor in mi placerat molestie. Ut et malesuada justo. Praesent at molestie lacus, non eleifend tortor. Aliquam non purus eleifend mi lobortis rutrum nec in quam. Sed gravida erat nec ligula feugiat maximus. Proin gravida purus quam, sit amet vehicula ex finibus sit amet. Vestibulum at facilisis augue. In quis rutrum leo, eget pellentesque nulla. Integer gravida urna tortor, non venenatis nibh malesuada in. Praesent vel aliquam nisl. Donec posuere diam non malesuada molestie "
    cumle3 = "Nullam suscipit nibh dictum turpis eleifend sollicitudin. Etiam sed viverra mauris. Suspendisse tincidunt, enim pharetra maximus pulvinar, sapien justo dapibus erat, sed eleifend nulla odio vel tortor. Donec eget feugiat lectus. Mauris iaculis, tellus ut porta finibus, sem ex rhoncus quam, feugiat dignissim eros risus id lacus. Nam pulvinar non diam sit amet faucibus. Ut elit massa, volutpat eu leo vel, aliquam tristique nibh. Aenean auctor imperdiet sapien, dapibus imperdiet orci cursus vel. Mauris lacinia enim leo, sed elementum nunc sollicitudin eget. Ut non ligula nec nisi iaculis rutrum sed at arcu. Integer maximus lacinia odio a vestibulum. Phasellus et nisi eu ante porta rhoncus. Phasellus vitae volutpat leo. Vestibulum porttitor lacus sollicitudin faucibus imperdiet. Duis nec nunc ornare, ultrices sem vitae, venenatis lectus. Vivamus ut nunc vulputate, malesuada augue mollis, condimentum elit "
    cumle4 = "Nullam sit amet orci condimentum, venenatis urna vitae, laoreet elit. Proin nulla arcu, posuere at luctus tincidunt, condimentum vitae metus. Morbi nunc nisl, suscipit ac justo ut, lacinia eleifend dui. Nulla sit amet vehicula dolor. Quisque venenatis fringilla ante eu bibendum. Fusce metus odio, aliquam eget pellentesque ac, finibus a neque. Praesent sollicitudin erat ac condimentum faucibus "
    cumle5 = "In sed sollicitudin augue, sit amet congue turpis. In hac habitasse platea dictumst. Nullam sit amet ultricies quam. Fusce porta quam eu magna maximus posuere. Phasellus in iaculis nisl. Donec elementum tellus in orci molestie dignissim. In sit amet scelerisque arcu. Duis placerat, nisi eget aliquam tempus, tortor elit interdum justo, et convallis est mauris in justo. Ut eu turpis fermentum, imperdiet arcu nec, molestie diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Mauris luctus laoreet libero, nec commodo elit blandit vitae. Suspendisse nulla velit, lacinia ac lacinia non, varius vel metus. Nunc vehicula mauris eget posuere dapibus. Proin pellentesque urna sed efficitur cursus."
    cumle = cumle1 + cumle2 + cumle3 + cumle4 + cumle5
    cumlelistesi = cumle.split(' ')
    ad_verisi=['Süleyman','Rıza','Burak','Yusuf','Gülşah','Esin','Gülsen','Ahmet','Mehmet','Selçuk','Mahmut','Raşit','Hakan','Engin','Ayşe','Deniz','Bahri','Veli']
    soyad_verisi=['Sülünogulları','Albayrak','Bediroğluları','Siyamiler','Deniz','Sevenler','Aşık','Gün','Gündüz','Özcan','Koyuncu']
    dvz_cinsi=['TL','EUR','USD']
    unvan=['İnsaat','Yazılım','Temizlik','Gıda','Gayrimenkul','Eğitim']
    boollistesi = [True,False]
    resim_verisi=['Data','Resim']
    vergi_daireleri_verisi=['Sultanbeyli','Sancaktepe','Ümraniye','Sariyer','Üsküdar','Kadıköy','Beşiktaş','Pendik','Kartal']
    hesap_no_verisi=['11111111111','222222222','12345678912','54698712306','14568795412','5096586588']
    mail_verisi=['abc@cc.com','cc@cc.com','msn@cc.com','ee@gmail.com','aa@.sinsaat.com','veli@tanrıverdiinsaaat.com','asadc@cc.com','ddddasdsa@ssdd.com','dasasdsa@ssads.com','adlsm@ss.com','ddsada@wwers.com']
    dvzTlType=['9']

    for x in range(10000000):
            # c_bolge_kod= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
            # c_ozel_kod= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
            # c_tip_kod= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
            # c_grup_kod= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
            # c_masrafMerkezi= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
            # c_mhs_kod= "{}{}{}{}".format(random.choice(aa),random.choice(bb),random.choice(aa),random.choice(bb))
        c_unvan = random.choice(unvan)
        b = random.choice(cumlelistesi)
        c_ad = random.choice(ad_verisi)
        c_soyad = random.choice(soyad_verisi)
        # c_id = random.randint(1,50001)
        c_aktifPasif = random.randint(0,2)
        c_bakGostSekli = random.randint(0,2)

        c_dvzCinsi=random.choice(dvz_cinsi)
        c_dvzTL = random.choice(dvzTlType)
        c_dvzCinsi=random.choice(dvz_cinsi)
        c_dovizIslemKurCins = random.randint(1,6)
        c_kredi_limiti = random.randint(1,100000)
        c_dvz_kredi_limiti = random.randint(1,1000000)
        c_resim=random.choice(resim_verisi)
        c_vergi_dairesi=random.choice(vergi_daireleri_verisi)
        c_hesap_no=random.choice(hesap_no_verisi)
        c_chk_kod="{}{}{}{}".format(random.choice(aa),random.choice(aa),random.choice(bb),random.choice(bb))
        c_iskonto=random.randint(1,70)
        c_uygulanacak_sat_fiyati=random.randint(1,12)
        c_opsiyon_gunu=random.randint(1,30)
        c_odeme_gunu=random.randint(1,8)
        c_kdv_muaf = random.choice(boollistesi)
        c_kdv_muaf_Tevfikat = random.choice(boollistesi)
        c_kdv_muaf_ack=random.choice(b)
        c_formBaBsUnvan = random.choice(boollistesi)
        c_sirketEMail=random.choice(mail_verisi)
        c_sirketWebAdres=random.choice(mail_verisi)
        c_satIslemEMail=random.choice(mail_verisi)
        c_satAlmaIslemEMail=random.choice(mail_verisi)
        c_finIslemEMail=random.choice(mail_verisi)
        book=Cari(
              hesapKodu=b,
              unvan=c_unvan,
              ad=c_ad,
              soyad=c_soyad,
              aktifPasif=c_aktifPasif,
              bakGostSekli=c_bakGostSekli,
              dvzTL=c_dvzTL,
              dovizCinsi=c_dvzCinsi,
              dovizIslemKurCins=c_dovizIslemKurCins,
              krediLimiti=c_kredi_limiti,
              dvzKrediLimiti=c_dvz_kredi_limiti,
              resim=c_resim,
              vergiDairesi=c_vergi_dairesi,
              hesapNo=c_hesap_no,
              faturaChk=c_chk_kod,
              iskontoOran=c_iskonto,
              opsiyonGunu=c_opsiyon_gunu,
              odemeGunu=c_odeme_gunu,
              kulSatisFiyat=c_uygulanacak_sat_fiyati,
              chKodu=c_chk_kod,
              kdvTevfikatUygula=c_kdv_muaf_Tevfikat,
              kdvMuaf=c_kdv_muaf,
              kdvMuafAck=c_kdv_muaf_ack,
              formBaBsUnvan=c_formBaBsUnvan,
              sirketEMail=c_sirketEMail,
              sirketWebAdres=c_sirketWebAdres,
              satIslemEMail=c_satIslemEMail,
              satAlmaIslemEMail=c_satAlmaIslemEMail,
              finIslemEMail=c_finIslemEMail
             )
        book.save()
######
hesapKodu = cari_formu.cleaned_data.get('hesapKodu')
unvan = cari_formu.cleaned_data.get('unvan')
ad = cari_formu.cleaned_data.get('ad')
soyad = cari_formu.cleaned_data.get('soyad')
aktifPasif = cari_formu.cleaned_data.get('aktifPasif')
bakGostSekli = cari_formu.cleaned_data.get('bakGostSekli')
dvzTL = cari_formu.cleaned_data.get('dvzTL')
dovizCinsi = cari_formu.cleaned_data.get('dovizCinsi')
dovizIslemKurCins = cari_formu.cleaned_data.get('dovizIslemKurCins')
krediLimiti = cari_formu.cleaned_data.get('krediLimiti')
dvzKrediLimiti = cari_formu.cleaned_data.get('dvzKrediLimiti')
bolgeKod = cari_formu.cleaned_data.get('bolgeKod')
ozelKod = cari_formu.cleaned_data.get('ozelKod')
grupKod = cari_formu.cleaned_data.get('grupKod')
tipKod = cari_formu.cleaned_data.get('tipKod')
mhsKod = cari_formu.cleaned_data.get('mhsKod')
masrafMerkezi = cari_formu.cleaned_data.get('masrafMerkezi')
resim = cari_formu.cleaned_data.get('resim')
vergiDairesi = cari_formu.cleaned_data.get('vergiDairesi')
hesapNo = cari_formu.cleaned_data.get('hesapNo')
faturaChk = cari_formu.cleaned_data.get('faturaChk')
iskontoOran = cari_formu.cleaned_data.get('iskontoOran')
opsiyonGunu = cari_formu.cleaned_data.get('opsiyonGunu')
odemeGunu = cari_formu.cleaned_data.get('odemeGunu')
# odemePlani = cari_formu.cleaned_data.get('odemePlani')
kulSatisFiyat = cari_formu.cleaned_data.get('kulSatisFiyat')
chKodu = cari_formu.cleaned_data.get('chKodu')
kdvTevfikatUygula = cari_formu.cleaned_data.get('kdvTevfikatUygula')
kdvMuaf = cari_formu.cleaned_data.get('kdvMuaf')
kdvMuafAck = cari_formu.cleaned_data.get('kdvMuafAck')
formBaBsUnvan = cari_formu.cleaned_data.get('formBaBsUnvan')
sirketEMail = cari_formu.cleaned_data.get('sirketEMail')
sirketWebAdres = cari_formu.cleaned_data.get('sirketWebAdres')
satIslemEMail = cari_formu.cleaned_data.get('satIslemEMail')
satAlmaIslemEMail = cari_formu.cleaned_data.get('satAlmaIslemEMail')
finIslemEMail = cari_formu.cleaned_data.get('finIslemEMail')
cari, created = Cari.objects.get_or_create(#**cari_formu.cleaned_data)
    hesapKodu=hesapKodu,
    unvan=unvan,
    ad=ad,
    soyad=soyad,
    aktifPasif=aktifPasif,
    bakGostSekli=bakGostSekli,
    dvzTL=dvzTL,
    dovizCinsi=dovizCinsi,
    dovizIslemKurCins=dovizIslemKurCins,
    krediLimiti=krediLimiti,
    dvzKrediLimiti=dvzKrediLimiti,
    bolgeKod=bolgeKod,
    ozelKod=ozelKod,
    grupKod=grupKod,
    tipKod=tipKod,
    mhsKod=mhsKod,
    masrafMerkezi=masrafMerkezi,
    resim=resim,
    vergiDairesi=vergiDairesi,
    hesapNo=hesapNo,
    faturaChk=faturaChk,
    iskontoOran=iskontoOran,
    opsiyonGunu=opsiyonGunu,
    odemeGunu=odemeGunu,
    # odemePlani = odemePlani,
    kulSatisFiyat=kulSatisFiyat,
    chKodu=chKodu,
    kdvTevfikatUygula=kdvTevfikatUygula,
    kdvMuaf=kdvMuaf,
    kdvMuafAck=kdvMuafAck,
    formBaBsUnvan=formBaBsUnvan,
    sirketEMail=sirketEMail,
    sirketWebAdres=sirketWebAdres,
    satIslemEMail=satIslemEMail,
    satAlmaIslemEMail=satAlmaIslemEMail,
    finIslemEMail=finIslemEMail,
)
if created == False:
    raise forms.ValidationError("Bu kayıt db'de mevcut")
######
            aşağıdaki kodlar aynı işi yapıyor.
            cari = Cari.objects.filter(id = uuid).update(**cari_formu.cleaned_data)
            vs
            cari_formu.save()

            #------------------------------| Kodun tamamı
            cari_verisi = get_object_or_404(Cari, id = uuid)
            # ,initial={'bolgeKod': cari_verisi.bolgeKod}
            cari_formu = CariFormu(request.POST or None, request.FILES or None, instance = cari_verisi)

            if cari_formu.is_valid():
                try:
                    cari = Cari.objects.get(**cari_formu.cleaned_data)
                    raise forms.ValidationError("Bu kayıt db'de mevcut")
                except Cari.DoesNotExist:
                    # cari = Cari.objects.filter(id = uuid).update(**cari_formu.cleaned_data)
                    cari_formu.save()
                    messages.success(request,_("Başarıyla kaydedildi. ---****"))
                    return redirect("Cari:cari")
                except ValueError as e:
                    messages.warning(request,e)         
                except ValidationError as e:
                    messages.warning(request,e) 
                # cari_formu.save()
######
Kod1 = cariKod_formu.cleaned_data.get('Kod1')
######
    records_total = SysReferans.objects.all().exclude(Q(id=None)|Q(Kod=None)|Q(Aciklama1=None)|Q(Aciklama2=None)|Q(GrupKod=None)|Q(SayKod=None))
    records_filtered = records_total
    referans = SysReferans.objects.all().exclude(Q(id=None)|Q(Kod=None)|Q(Aciklama1=None)|Q(Aciklama2=None)|Q(GrupKod=None)|Q(SayKod=None)).count()
######
        referans = SysReferans.objects.filter(
                        Q(id__icontains=search)|
                        Q(Kod__icontains=search)|
                        Q(Aciklama1__icontains=search)|
                        Q(Aciklama2__icontains=search)|
                        Q(GrupKod__icontains=search)|
                        Q(SayKod__icontains=search)
                     ).exclude(Q(id=None)|Q(Kod=None)|Q(Aciklama1=None)|Q(Aciklama2=None)|Q(GrupKod=None)|Q(SayKod=None))
######
def initFormFieldSettings(columns,self,formName):
    # sysColumns'ta visible özelliğine göre disable ayarlarını yapar.
    if col != True:
        self.fields[name].widget = forms.HiddenInput()
        self.fields[name].label ="" 
        # self.fields[name].disabled = False 
                
######
python manage.py rename demo <new-project-name>     -- project ismi değişmek için
[kaynak](https://www.youtube.com/watch?v=z4USlooVXG0&list=PLLRM7ROnmA9F2vBXypzzplFjcHUaKWWP5)
######
allauth
[kaynak](https://django-allauth.readthedocs.io/en/latest/installation.html  )
######
Django extensions 
Graph models
[Kaynak](https://django-extensions.readthedocs.io/en/latest/graph_models.html)
######
html = render(request, 'apps/responses/validity_error_response.html', context)
html.set_cookie("isim","selçuk")
return html
Kaynak : https://medium.com/better-programming/managing-cookies-in-django-34981d9bf0ae
Kaynak : https://data-flair.training/blogs/django-cookies-handling/
######
convert javascript object to json and send django view
kaynak : https://stackoverflow.com/questions/56809178/django-how-do-i-properly-send-a-list-from-template-to-ajax-to-view
######
Signals
kaynak:https://docs.djangoproject.com/en/2.2/topics/signals/
Receiver functions
def my_callback(sender, **kwargs):
    print("Request finished!")
Connecting receiver functions
1. yol
from django.core.signals import request_finished

request_finished.connect(my_callback)
2. yol
from django.core.signals import request_finished
from django.dispatch import receiver

@receiver(request_finished)
def my_callback(sender, **kwargs):
    print("Request finished!")
- Now, our my_callback function will be called each time a request finishes.


######
extend django user
kaynak : https://github.com/Django-Pyhon/eCommerce/blob/c698e75c82b6145546c93f8d32fec616dfaf1cac/src/accounts/models.py
class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True)
    # full_name   = models.CharField(max_length=255, blank=True, null=True)
    active      = models.BooleanField(default=True) # can login 
    staff       = models.BooleanField(default=False) # staff user non superuser
    admin       = models.BooleanField(default=False) # superuser 
    timestamp   = models.DateTimeField(auto_now_add=True)
    # confirm     = models.BooleanField(default=False)
    # confirmed_date     = models.DateTimeField(default=False)

    USERNAME_FIELD = 'email' #username
    # USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #['full_name'] #python manage.py createsuperuser

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
######
How to Reset Migrations
source : https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
Scenario 1:
Go through each of your projects apps migration folder and remove everything inside, except for the __init__.py file.
Or if you are using a unix-like OS you can run the following script (inside your project dir):
1. Remove the all migrations files within your project
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
2. Drop the current database, or delete the db.sqlite3 if it is your case.
3. Create the initial migrations and generate the database schema:
```
python manage.py makemigrations
python manage.py migrate
```
Scenario 2:
1. Make sure your models fits the current database schema
```
python manage.py makemigrations
```
2. Clear the migration history for each app
```
$ python manage.py showmigrations
```
```
python manage.py migrate --fake core zero
```
3. Remove the actual migration files.
Go through each of your projects apps migration folder and remove everything inside, except for the __init__.py file.
```
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```
```
$ python manage.py showmigrations
```
4. Create the initial migrations
```
$ python manage.py makemigrations
```
5. Fake the initial migration
In this case you won’t be able to apply the initial migration because the database table already exists. What we want to do is to fake this migration instead:
```
$ python manage.py migrate --fake-initial
```

######
Check permission inside a template in Django
kaynak : https://stackoverflow.com/questions/9469590/check-permission-inside-a-template-in-django
######
xhtml2pdf türkçe karakter sorunu
https://stackoverflow.com/questions/45689236/django-pdf-response-has-wrong-encoding-xhtml2pdf
######
windows bulunan bir pcye kali yüklenirse ve grub windows görmez ise aşağıdaki kod uygulanabilir
grub-mkconfig -o /boot/grub/grub.cfg
kaynak : https://unix.stackexchange.com/questions/309759/windows-10-is-not-showing-in-grub2-after-kali-linux-install
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######
######


