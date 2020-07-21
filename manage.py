from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from zlbbs import create_app
from exts import db
from apps.cms import models as cms_models
from apps.front import models as front_models
from apps.models import BannerModel, BoardModel, PostModel, CommentModel, HighlightPostModel

CMSUser = cms_models.CMSUser
CMSRole = cms_models.CMSRole
CMSPersmission = cms_models.CMSPersmission
FrontUser = front_models.FrontUser
app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-e', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CMSUser(username=username, password=password, email=email)
    try:
        db.session.add(user)
        db.session.commit()
        print("cms用户添加成功")
    except Exception as e:
        print(e)


@manager.command
def create_role():
    # 1.访问者，可以修改信息
    visitor = CMSRole(name='访问者', desc='修改个人信息')
    visitor.permissions = CMSPersmission.VISITOR
    # 2.运营角色(修改个人信息，管理评论，帖子，管理前台用户)
    operator = CMSRole(name='运营', desc='管理评论，帖子，管理前台用户')
    operator.permissions = CMSPersmission.VISITOR | CMSPersmission.POSTER | CMSPersmission.COMMENTER | CMSPersmission.FORNTUSER
    # 3.管理员(拥有绝大部分权限)
    admin = CMSRole(name='管理员', desc='拥有所有权限')
    admin.permissions = CMSPersmission.VISITOR | CMSPersmission.POSTER | CMSPersmission.COMMENTER | CMSPersmission.FORNTUSER | CMSPersmission.BOARDER | CMSPersmission.CMSUSER
    # 4.开发人员
    developer = CMSRole(name='开发人员', desc='开发者专用')
    developer.permissions = CMSPersmission.ALL_PERMISSION
    db.session.add_all([visitor, operator, admin, developer])


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_to_role(email, name):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        role = CMSRole.query.filter_by(name=name).first()
        if role:
            role.users.append(user)
            print('用户添加到角色成功')
        else:
            print('没有这个角色:%s' % role)
    else:
        print('%s邮箱没有这个用户' % user)


@manager.option('-t', '--telephone', dest='telephone')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
def create_front_user(telephone, username, password):
    user = FrontUser(telephone=telephone, username=username, password=password)
    db.session.add(user)


@manager.command
def create_test_post():
    for x in range(1, 205):
        title = "标题%s" % x
        content = "内容：%s" % x
        board = BoardModel.query.first()
        author = FrontUser.query.first()
        post = PostModel(title=title, content=content)
        post.board = board
        post.author = author
        db.session.add(post)
    print("测试帖子添加成功")


if __name__ == '__main__':
    manager.run()
