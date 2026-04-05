from playwright.sync_api import Page, expect


class EmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_info = page.get_by_test_id("section:mailbox_name")
        self.user_info_txt = self.user_info.locator("div").first.locator("small")
        self.send_email_btn = page.get_by_test_id("btn:newMail_action")
        self.logout_btn = page.get_by_test_id("btn:switchAccount_action")
        self.new_email_dialog = page.get_by_role("dialog")
        self.received_emails = page.get_by_test_id("unordered_list")
        # TODO: create a separate component?
        self.send_to = page.get_by_test_id("tfi:to_label")
        self.send_from = page.get_by_test_id("tfi:sender_label")
        self.subject = page.get_by_test_id("tfi:subject_label")
        self.message = page.get_by_test_id("text_editor")
        self.send_btn = page.get_by_test_id("btn:send_action")

    def is_loaded(self):
        # TODO: check if correct email address is visible?
        self.user_info.wait_for(state='visible')
        self.send_email_btn.wait_for(state='visible')
        expect(self.send_email_btn).to_be_visible()

    def send_mail(self, email: str, subject="Interesting subject"):
        self.send_email_btn.click()
        self.new_email_dialog.wait_for(state='visible')
        self.send_to.click()
        # As only one email was created for this project, mail is sent to the same email address
        self.send_to.fill(email)
        expect(self.send_from).to_contain_text(email)
        self.subject.click()
        self.subject.fill(subject)
        self.message.click()
        self.message.fill("Interesting message")
        self.send_btn.click()

    def mail_received(self, subject="Interesting subject"):
        expect(self.received_emails).to_contain_text(subject)

    def logout(self):
        self.logout_btn.click()
