from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, photo=None, title=None,
                 company=None, address=None, home_tel=None, mobile_tel=None, work_tel=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, b_day=None, b_month=None, b_year=None, anny_day=None, anny_month=None, anny_year=None,
                 group=None, address2=None, phone2=None, notes=None, cont_id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.home_tel = home_tel
        self.mobile_tel = mobile_tel
        self.work_tel = work_tel
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.b_day = b_day
        self.b_month = b_month
        self.b_year = b_year
        self.anny_day = anny_day
        self.anny_month = anny_month
        self.anny_year = anny_year
        self.group = group
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.cont_id = cont_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.cont_id, self.last_name, self.first_name, self.work_tel, self.mobile_tel)

    def __eq__(self, other):
        return (self.cont_id is None or other.cont_id is None or self.cont_id == other.cont_id) \
               and self.last_name == other.last_name \
                and self.first_name == other.first_name


    def id_or_max(gr):
        if gr.cont_id:
            return int(gr.cont_id)
        else:
            return maxsize