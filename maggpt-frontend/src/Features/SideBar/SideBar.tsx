import './SideBar.scss'

import profile from './Assets/profile.svg';
import pen from './Assets/pen.svg';
import ButtonEvent from "../../Shared/ButtonEvent/ButtonEvent.tsx";

function SideBar() {

    return (
        <div className="sidebar">

            <div className="sidebar__container">
                <h1>MagGPT</h1>
                <ButtonEvent link={'/'} style={{marginTop: '40px', marginBottom: '10px'}} image={pen} title={'Новый чат'}/>
            </div>


            <div className="chats">
                <p className="chats__title">Чаты</p>
                <ul className="chats__list">
                    <li>
                        <ButtonEvent link={'/1'} style={{marginTop: '10px'}}  title={`Lorem ipsum dolor sit amet.`}/>
                    </li>
                </ul>
            </div>

            <a href="#" className="profile">
                <img className="profile__icon" src={profile}/>
                <p className="profile__name">Лущенко Алексейппппппппппппп</p>
            </a>
        </div>
    )
}

export default SideBar
