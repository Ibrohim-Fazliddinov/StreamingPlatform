'use client';
import { useState, useEffect } from 'react';
import styles from './MovieTrend.module.css';

export default function MovieTrend() {
    const [isHovered, setIsHovered] = useState(false);
    const [isShow, setIsShow] = useState(false);
    const [swiperSlideEl, setSwiperSlideEl] = useState(null);
    useEffect(() => {
        if (isHovered) {
            const timer = setTimeout(() => {
                setIsShow(true);
            }, 2000);
            return () => clearTimeout(timer);
        }
        if (!isHovered) setIsShow(false);
    }, [isHovered]);
    return (
        <div
            onMouseEnter={(e) => {
                if (!swiperSlideEl) {
                    setSwiperSlideEl(e.target?.offsetParent);
                }

                e.target.offsetParent.style.zIndex = 10;
                setIsHovered(true);
            }}
            onMouseLeave={(e) => {
                setIsHovered(false);
                swiperSlideEl.style.zIndex = -1;
            }}
        >
            <div className={styles.wrapper}>
                <div className={styles.preview}></div>{' '}
                <div className={styles.info}>
                    <div className={styles.title}>The white house</div>
                    <div className={styles.details}>
                        <div className={styles.year}>2023</div>
                        <div className={styles.duration}>2h 35 mins</div>
                        <div className={styles.restriction}>TV-MA</div>
                    </div>
                </div>
            </div>
            <div
                className={
                    !isShow ? styles.modal : `${styles.modal} ${styles.zoom}`
                }
            >
                <div className={styles.details}>
                    <div className={styles.year}>2023</div>
                    <div className={styles.duration}>2h 35 mins</div>
                    <div className={styles.restriction}>TV-MA</div>
                </div>
            </div>
        </div>
    );
}
