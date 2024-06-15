"""
Reference
hayashi-ay: https://github.com/hayashi-ay/leetcode/pull/25/files
fhiyo: https://github.com/fhiyo/leetcode/pull/17/files
goto-untrapped: https://github.com/goto-untrapped/Arai60/pull/8/files
nittoco: https://github.com/nittoco/leetcode/pull/7/files

う~~~~ん, こうしてみるとphase1には明らかな問題があります
1. split_email_strings.append(email[prev_cursor:cursor])のところが少しパズルな気がする。
part_of_local_name = email[prev_cursor:cursor]として
split_email_strings.append(part_of_local_name)としたほうが何を保存してくれているのかわかってよさそう
あとはprev_cursor:cursorもleft:rightぐらいの命名の方が欲しい区間を取り出してるんだな感がでそう
split_email_stringsよりも, part_of_valid_emailとかの方が保存しているものにも合うかな
問題文を参考に変数名を決める癖, 処理に応じて連想されやすい名前をつけた方がいい気がしました

2. local nameの"."の処理がやや不安
例えばa.b.c.d.e.f.g.h.i.j.k.l.m.n@gmail.comみたいなメルアドだと何回もemail[prev_cursor:cursor]が呼ばれて無駄な処理が増えます。実際, やや遅いテストケースもある気がします

他の懸念事項(https://github.com/TORUS0818/leetcode/pull/16/files)
@がない場合: エラーにしたい
@が複数の場合: wikiを見る限りquoted-stringの中身ならエラーを出さない方が良い...?(プロバイダによる)
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.rsplit("@", maxsplit = 1)
            local_name = local_name.replace(".", "")
            local_name = local_name.split("+", maxsplit = 1)[0]
            unique_emails.add(f'{local_name}@{domain_name}')
        return len(unique_emails)
