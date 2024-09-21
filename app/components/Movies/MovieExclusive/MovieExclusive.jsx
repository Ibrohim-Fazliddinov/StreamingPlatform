import styles from './MovieExclusive.module.css';

export default function MovieExclusive() {
    return (
        <div className={styles.wrapper}>
            <div className={styles.preview}></div>
            <div className={styles.title}>Love and War</div>
            <div className={styles.details}>
                <div className={styles.view}>815 views</div>
                <div className={styles.season}>1 Season</div>
            </div>
        </div>
    );
}
