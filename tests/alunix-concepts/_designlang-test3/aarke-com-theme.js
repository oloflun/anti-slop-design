// React Theme — extracted from https://aarke.com
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
 *   };
 *   fonts: {
    body: string;
    heading: string;
 *   };
 *   fontSizes: {
    '9': string;
    '10': string;
    '12': string;
    '14': string;
    '16': string;
    '20': string;
    '22': string;
    '28': string;
    '10.0002': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '28': string;
    '32': string;
    '36': string;
    '40': string;
    '48': string;
    '57': string;
    '64': string;
    '128': string;
    '290': string;
    '316': string;
    '334': string;
 *   };
 *   radii: {
    lg: string;
    full: string;
 *   };
 *   shadows: {
    md: string;
    xl: string;
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
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#3c3c3c",
    "neutral300": "#efefef",
    "neutral400": "#adadad",
    "neutral500": "#101010"
  },
  "fonts": {
    "body": "'Button Font', sans-serif",
    "heading": "'Heading Font', sans-serif"
  },
  "fontSizes": {
    "9": "9px",
    "10": "10px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "20": "20px",
    "22": "22px",
    "28": "28px",
    "10.0002": "10.0002px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "28": "28px",
    "32": "32px",
    "36": "36px",
    "40": "40px",
    "48": "48px",
    "57": "57px",
    "64": "64px",
    "128": "128px",
    "290": "290px",
    "316": "316px",
    "334": "334px"
  },
  "radii": {
    "lg": "12px",
    "full": "50px"
  },
  "shadows": {
    "md": "rgba(0, 0, 0, 0.1) 0px 4px 10px 0px",
    "xl": "rgba(0, 0, 0, 0.2) 0px 26px 80px 0px"
  },
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
    "background": {
      "default": "#ffffff",
      "paper": "#ebebeb"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'Button Font', sans-serif",
    "h2": {
      "fontSize": "28px",
      "fontWeight": "500",
      "lineHeight": "33px",
      "fontFamily": "'Heading Font', sans-serif"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "35px",
      "fontFamily": "'Heading Font', sans-serif"
    },
    "body1": {
      "fontSize": "16px",
      "fontWeight": "300",
      "lineHeight": "20.8px"
    },
    "body2": {
      "fontSize": "12px",
      "fontWeight": "300",
      "lineHeight": "15px"
    }
  },
  "shape": {
    "borderRadius": 12
  },
  "shadows": [
    "rgba(0, 0, 0, 0.1) 0px 4px 10px 0px",
    "rgba(0, 0, 0, 0.2) 0px 26px 80px 0px"
  ]
};

export default theme;
