import styles from './MovieRecommended.module.css';

export default function MovieRecommended() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.preview}></div>
            <div className={styles.title}>Love and War</div>
            <div className={styles.details}>
                <div className={styles.year}>2020</div>
                <div className={styles.season}>1 Season</div>
            </div>
        </div>
    );
}
