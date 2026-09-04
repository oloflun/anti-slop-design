// React Theme — extracted from https://www.diablaoutdoor.com/en/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
 *   };
 *   fonts: {
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '10': string;
    '12': string;
    '14': string;
    '16': string;
    '20': string;
    '28': string;
    '30': string;
    '60': string;
    '90': string;
    '19.2': string;
    '13.3333': string;
 *   };
 *   space: {
    '1': string;
    '15': string;
    '30': string;
    '40': string;
    '52': string;
    '60': string;
    '80': string;
    '100': string;
    '150': string;
    '326': string;
    '382': string;
    '480': string;
 *   };
 *   radii: {
    lg: string;
    full: string;
 *   };
 *   shadows: {

 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#fcf0f3",
    "secondary": "#007aff",
    "accent": "#ff4f55",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#333333",
    "neutral300": "#808080"
  },
  "fonts": {
    "body": "'Arial', sans-serif",
    "heading": "'LinotypeHelveticaNeueLTStdLt', sans-serif"
  },
  "fontSizes": {
    "10": "10px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "28": "28px",
    "30": "30px",
    "60": "60px",
    "90": "90px",
    "19.2": "19.2px",
    "13.3333": "13.3333px"
  },
  "space": {
    "1": "1px",
    "15": "15px",
    "30": "30px",
    "40": "40px",
    "52": "52px",
    "60": "60px",
    "80": "80px",
    "100": "100px",
    "150": "150px",
    "326": "326px",
    "382": "382px",
    "480": "480px"
  },
  "radii": {
    "lg": "12px",
    "full": "100px"
  },
  "shadows": {},
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#fcf0f3",
      "light": "hsl(345, 67%, 95%)",
      "dark": "hsl(345, 67%, 81%)"
    },
    "secondary": {
      "main": "#007aff",
      "light": "hsl(211, 100%, 65%)",
      "dark": "hsl(211, 100%, 35%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#fcf0f3"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ed2e38"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "60px",
      "fontWeight": "400",
      "lineHeight": "50px",
      "fontFamily": "'LinotypeHelveticaNeueLTStdLt', sans-serif"
    },
    "h2": {
      "fontSize": "28px",
      "fontWeight": "400",
      "lineHeight": "31px",
      "fontFamily": "'LinotypeHelveticaNeueLTStdLt', sans-serif"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "22px",
      "fontFamily": "'LinotypeHelveticaNeueLTStdLt', sans-serif"
    },
    "body1": {
      "fontSize": "19.2px",
      "fontWeight": "400",
      "lineHeight": "18px"
    }
  },
  "shape": {
    "borderRadius": 12
  },
  "shadows": []
};

export default theme;
