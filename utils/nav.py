from dash import dcc, html


def li_icon_link(name, href, icon_class, link_id):
    '''创建带有 icon 的标题栏的项'''
    link = dcc.Link(name,
                    href=href,
                    id=link_id)
    icon = html.I(link, className=icon_class)
    return html.Li(icon, className='w3-padding-small w3-button app-button')


def page_nav():
    '''创建页面菜单栏'''
    home = li_icon_link('主页', '/',
                        'fas fa-home',
                        link_id='home-link')
    record = li_icon_link('记录', '/record',
                          'fas fa-film',
                          link_id='record-link')
    watch = li_icon_link('监测', '/watch',
                          'far fa-file-video',
                          link_id='watch-link')
    replay = li_icon_link('回放', '/replay',
                          'far fa-play-circle',
                          link_id='replay-link')
    about = li_icon_link('关于', '/about',
                         'fas fa-user-circle',
                         link_id='about-link')

    ul = html.Ul([home, record, replay, watch, about], className='w3-padding-small')
    nav = html.Nav(ul, className='w3-pale-blue w3-padding-small w3-bottombar')
    return nav


def page_header(title='Sanstyle Dash'):
    '''创建页面导航栏'''
    title = html.H1(title, className='w3-opacity-max w3-right')
    header_nav = page_nav()
    return html.Header([title, header_nav])
