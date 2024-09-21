import styles from './MovieRelease.module.css';

export default function MovieRelease() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.preview}></div>
            <div className={styles.info}>
                <div className={styles.title}>John Wick 4</div>
                <div className={styles.details}>
                    <div className={styles.detailsLeft}>
                        <div className={styles.year}>2023</div>
                        <div className={styles.duration}>1h 25 mins</div>
                    </div>
                    <div className={styles.detailsRight}>
                        <div className={styles.restriction}>TV-MA</div>
                    </div>
                </div>
                <div className={styles.genres}>
                    <span className={styles.genre}>Action</span>{' '}
                    <span className={styles.genre}>Thriller</span>
                </div>
            </div>
        </div>
    );
}
