import Image from 'next/image';
import styles from './MainPreviewContent.module.css';
import PlayIcon from '/public/icons/play.svg';
import BookmarkIcon from '/public/icons/bookmark.svg';
import ButtonGradient from '../UI/ButtonGradient/ButtonGradient';
export default function MainPreviewContent() {
    return (
        <>
            <div className={styles.wrapper}>
                <div className={styles.genres}>ACTION,THRILLER</div>
                <div className={styles.nameOfMovie}>John Wick 4</div>
                <div className={styles.movieInfo}>
                    <div className={styles.star}>
                        {
                            <Image
                                src={'/icons/star.svg'}
                                width={14}
                                height={14}
                                className={styles.starIcon}
                                alt={'star'}
                            />
                        }
                    </div>
                    <div className={styles.grade}>6.2</div>
                    <div className={styles.year}>2023</div>
                    <div className={styles.durationFilm}>1 hr 25 mins</div>
                    <div className={styles.restriction}>TV-MA</div>
                </div>
                <div className={styles.descr}>
                    Enjoy exclusive Amazon Originals as well as popular movies
                    and TV shows for USD 120z/month. Watch now, cancel anytime.
                </div>
                <div className={styles.actions}>
                    <ButtonGradient
                        text={'Play Now'}
                        icon={<PlayIcon />}
                        isAnimationIcon={false}
                    />
                    <button className={styles.watchLater}>
                        <span className={styles.watchLaterText}>
                            Watch Later
                        </span>
                        <span>
                            <BookmarkIcon className={styles.bookmarkIcon} />
                        </span>
                    </button>
                </div>
            </div>
        </>
    );
}
