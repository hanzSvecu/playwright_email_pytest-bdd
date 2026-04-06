from pathlib import Path

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
        self.select_all_emails = page.get_by_test_id("cb:selectAllLoaded_action")
        self.delete_selected = page.get_by_test_id("btn:trash_action")
        self.mailbox_empty_picture = page.get_by_test_id("message_box:noMails_msg")
        self.attach_btn = page.get_by_test_id("btn:attachFiles_action")
        self.file_chooser = page.locator('input[type="file"]')
        self.first_email = page.get_by_role("listitem").first
        self.has_attachment_icon = page.get_by_test_id("btn:attachment_name")
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

    def send_mail(self, email: str, with_attachment: bool = False, subject="Interesting subject"):
        self.send_email_btn.click()
        self.new_email_dialog.wait_for(state="visible")

        self.send_to.fill(email)
        expect(self.send_from).to_contain_text(email)
        self.subject.fill(subject)
        self.message.fill("Interesting message")

        if with_attachment:
            with self.page.expect_file_chooser() as fc_info:
                self.attach_btn.click()
            file_chooser = fc_info.value
            file_path = Path("tests/test_data/funny_attachment.png").resolve()
            file_chooser.set_files(file_path)
            expect(self.new_email_dialog.get_by_text("funny_attachment.png")).to_be_visible(timeout=15000)
        self.send_btn.click()

    #TODO: verify functionality
    def mail_received(self, with_attachment: bool = False, subject="Interesting subject"):
        # email_item = self.received_emails.filter(has_text=subject).first
        # expect(email_item).to_be_visible(timeout=300000)
        # expect(email_item).to_be_enabled(timeout=10000)
        #
        # email_item.click(trial=True, timeout=10000)
        # email_item.click()

        # expect(self.page.get_by_text(subject, exact=True)).to_be_visible(timeout=10000)

        email_row = self.page.locator('li.list-row').filter(has_text=subject).first
        expect(email_row).to_be_visible(timeout=300000)
        email_row.click(trial=True, timeout=10000)

        if with_attachment:
            email_row.click()
            expect(self.page.get_by_text("funny_attachment.png")).to_be_visible(timeout=10000)

    def delete_emails(self):
        if self.mailbox_empty_picture.is_visible():
            expect(self.mailbox_empty_picture).to_be_visible()
            return

        expect(self.select_all_emails).to_be_visible(timeout=10000)
        expect(self.select_all_emails).to_be_enabled(timeout=10000)
        self.select_all_emails.check(trial=True, timeout=10000)
        self.select_all_emails.check()
        expect(self.select_all_emails).to_be_checked(timeout=5000)

        expect(self.delete_selected).to_be_visible(timeout=10000)
        expect(self.delete_selected).to_be_enabled(timeout=10000)
        self.delete_selected.click(trial=True, timeout=10000)
        self.delete_selected.click()

        expect(self.mailbox_empty_picture).to_be_visible(timeout=15000)

    def logout(self):
        self.logout_btn.click()
