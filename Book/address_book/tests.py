from django.contrib.sites import requests
from django.test import TestCase
from address_book.models import Contact


class AddressTestCase(TestCase):

    def setUp(self):
        Contact.objects.create(name="Swapnil", phone="(201)548-7210")
        Contact.objects.create(name="Sudhir", phone="(201)548-5454")

    def test_phone(self):
        swapnil = Contact.objects.get(name="Swapnil")
        sudhir = Contact.objects.get(name="Sudhir")
        self.assertEqual(swapnil.phone, '(201)548-7210')
        self.assertEqual(sudhir.phone, '(201)548-5454')

    def test_post(self):
        id=Contact.objects.get(name="Swapnil").id
        resp =self.client.post("/address/updatedata/"+str(id),
                               {'name':"Swapnil", 'phone':"(201)548-0000"})
        self.assertEqual(resp.status_code, 200)
        swapnil = Contact.objects.get(name="Swapnil")
        self.assertEqual(swapnil.phone, '(201)548-0000')

    def test_delete(self):
        id=Contact.objects.get(name="Swapnil").id
        resp =self.client.delete("/address/deletedata/"+str(id))
        print(resp.status_code)
        # swapnil = Contact.objects.get(name="Swapnil")
        self.assertEqual(resp.status_code, 302)
